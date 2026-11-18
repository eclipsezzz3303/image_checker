from image_checker import check_image, summarize
import pytest

@pytest.mark.parametrize("filename, status, width, height, fmt", [
    ("images/photo1.jpg", "ok",        640,  480,  "JPEG"), 
    ("images/photo2.png", "ok",        1920, 1080, "PNG"),
    ("images/photo3.jpg", "ok",        100,  100,  "JPEG"), 
    ("images/broken.jpg", "broken",    None, None, None),
    ("images/notes.txt",  "not_image", None, None, None), 
])
def test_check_images(filename, status, width, height, fmt):
    result = check_image(filename)
    assert result["status"] == status
    assert result["width"]  == width
    assert result["height"] == height
    assert result["format"] == fmt

def test_summarize():                                                                                                                                                                                                                                               
      """summarize 应正确统计各状态数量"""                                                                                                                                                                                                                            
      fake_results = [                                                                                                                                                                                                                                                
          {"status": "ok"},                                                                                                                                                                                                                                           
          {"status": "ok"},                                                                                                                                                                                                                                           
          {"status": "ok"},                                                                                                                                                                                                                                           
          {"status": "broken"},                                                                                                                                                                                                                                       
          {"status": "not_image"},                                                                                                                                                                                                                                    
      ]                                                                                                                                                                                                                                                               
      summary = summarize(fake_results)                                                                                                                                                                                                                               
      assert summary["total"] == 5                                                                                                                                                                                                                                    
      assert summary["ok"] == 3                                                                                                                                                                                                                                       
      assert summary["broken"] == 1                                                                                                                                                                                                                                   
      assert summary["not_image"] == 1 