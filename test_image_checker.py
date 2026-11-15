from image_checker import check_image, summarize
import pytest

# def test_check_image_good():
#     result = check_image("images/photo1.jpg")
#     assert result["status"] == "ok"
#     assert result["width"] == 640
#     assert result["height"] == 480
#     assert result["format"] == "JPEG"

# def test_check_image_broken():
#     result = check_image("images/broken.jpg")
#     assert result["status"] == "broken"
#     assert result["width"] is None

@pytest.mark.parametrize("filename, status, width, height, format", [
    ("images/photo1.jpg", "ok",        640,  480,  "JPEG"), 
    ("images/photo2.png", "ok",        1920, 1080, "PNG"),
    ("images/photo3.jpg", "ok",        100,  100,  "JPEG"), 
    ("images/broken.jpg", "broken",    None, None, None),
    ("images/notes.txt",  "not_image", None, None, None), 
])
def test_check_images(filename, status, width, height, format):
    result = check_image(filename)
    assert result["status"] == status
    assert result["width"]  == width
    assert result["height"] == height
    assert result["format"] == format

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