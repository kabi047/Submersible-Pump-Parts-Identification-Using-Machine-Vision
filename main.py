import cv2
import numpy as np
from ultralytics import YOLO
import sys
import os
import time

class PumpSystem:
    def __init__(self):
        # --- PATH SETUP ---
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))
            
        self.model_path = os.path.join(base_path, 'best.pt')

        # --- LOAD MODEL ---
        print(f"✅ Loading Brain: {self.model_path}")
        try:
            self.model = YOLO(self.model_path)
            # DEBUG: Print what the model knows
            print("🧠 Model Classes Loaded:")
            print(self.model.names) 
        except Exception as e:
            print(f"CRITICAL ERROR: {e}")
            input("Press Enter to exit...")
            sys.exit(1)

        # --- CAMERA SETUP (1280x720) ---
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def run(self):
        print("--- DEBUG MODE RUNNING ---")
        print("Tracking: OFF (Fresh guess every frame)")
        print("Press 'q' to quit.")
        
        while True:
            success, frame = self.cap.read()
            if not success: break

            start_time = time.time()

            # --- INFERENCE ---
            # persist=False: Forces the AI to think fresh every frame (Fixes "Sticky Label" bug)
            # conf=0.25: Lowered slightly to see if the "Right" class is just below 50%
            results = self.model.predict(
                frame, 
                imgsz=640, 
                conf=0.25, 
                device=0, 
                verbose=False,
                retina_masks=True
            )
            
            # --- VISUALIZATION ---
            if results[0].masks is not None:
                masks = results[0].masks.data.cpu().numpy()
                boxes = results[0].boxes.data.cpu().numpy()
                
                for i, mask in enumerate(masks):
                    class_id = int(boxes[i][5])
                    score = float(boxes[i][4])
                    part_name = self.model.names[class_id]
                    
                    # Resize mask to 1280x720 to match the window
                    mask = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
                    
                    # Draw Contour
                    contours, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
                    
                    # Label
                    x, y, x2, y2 = boxes[i][:4].astype(int)
                    label = f"{part_name} {int(score*100)}%"
                    
                    # Draw text
                    cv2.rectangle(frame, (x, y - 30), (x + 200, y), (0, 0, 0), -1)
                    cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            # FPS
            fps = 1.0 / (time.time() - start_time)
            cv2.putText(frame, f"FPS: {int(fps)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            cv2.imshow("Pump Inspector DEBUG", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = PumpSystem()
    app.run()