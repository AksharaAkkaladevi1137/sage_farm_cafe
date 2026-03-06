from PIL import Image
import os
import glob

assets_dir = r"c:\Users\Akshara.Akkaladevi\Desktop\SAGE Farm cafe\assets"
files = glob.glob(os.path.join(assets_dir, "*.*"))

for f in files:
    if f.endswith('.py'): continue
    ext = os.path.splitext(f)[1].lower()
    if ext not in ['.png', '.jpg', '.jpeg', '.webp']: continue
    
    try:
        img = Image.open(f)
        # Force load to ensure file can be closed
        img.load()
        
        base, ext = os.path.splitext(f)
        new_path = base + ".webp"
        
        # Save as webp with compression
        img.save(new_path, "WEBP", quality=50, method=4)
        print(f"Compressed {new_path}")
        
        img.close()
        
        # Remove original if format changed
        if f != new_path:
            os.remove(f)
            print(f"Removed original {f}")
            
    except Exception as e:
        print(f"Error processing {f}: {e}")
