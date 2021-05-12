from tf_analysis.model import *
from tf_analysis.data import *  # 导入这两个文件中的所有函数
import matplotlib.pyplot as plt
import cv2
from skimage import io
from db.sqlite3_connect import insert_data, select_data, create_table


def post_analysis(file):

    # tensorflow predict results
    test_image_path = '%s' % file

    num_class = 3
    model = unet()
    model.load_weights('tf_analysis/unet_2_100_40.hdf5')
    testGene = testGenerator(test_image_path, num_image=1, flag_multi_class=True, as_gray=False)
    results = model.predict_generator(testGene, 1, verbose=1)
    from skimage import img_as_ubyte
    dst = img_as_ubyte(results)
    saveResult("appimage/wound_image/wound_label", dst)

    # opencv draw contour
    from PIL import Image
    test_image = Image.open(r"appimage/wound_image/input_wound/0.png")  # 打开image
    test_image = test_image.convert("RGB")  # 4通道转化为rgb三通道
    test_image = test_image.resize((256, 256), Image.ANTIALIAS)
    test_image.save(r"appimage/wound_image/wound_label/wound_resize/resize.png")
    ori = cv2.imread(r"appimage/wound_image/wound_label/wound_resize/resize.png")
    w1 = cv2.imread(r"appimage/wound_image/wound_label/0_predict.png")

    gaus = cv2.GaussianBlur(w1, (3, 3), 0, 0)
    gray = cv2.cvtColor(gaus, cv2.COLOR_BGR2GRAY)
    edge_output = cv2.Canny(gray, 50, 300)

    gray = cv2.cvtColor(w1, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(edge_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    n = len(contours)
    contoursImg = []
    area = []
    for i in range(n):
        print("contours[" + str(i) + "]面积=", cv2.contourArea(contours[i]), " || 周长=", cv2.arcLength(contours[i], True))
        a = cv2.contourArea(contours[i])
        area.append(a)
        temp = np.zeros(w1.shape, np.uint8)
        contoursImg.append(temp)
        contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 3)
        # 筛选出最大面积的位置
        max_id = np.argmax(area)
        if i == n - 1:
            w1 = cv2.drawContours(ori, contours, max_id, (0, 0, 255), 3)
            cv2.imwrite("appimage/wound_image/output_wound/result.png", w1)
            max_area = cv2.contourArea(contours[max_id])
            max_perimeter = cv2.arcLength(contours[max_id], True)
            sql = "UPDATE report SET area='" + str(max_area) + "',perimeter='" + str(max_perimeter) + "' WHERE id = 1"
            print(sql)
            insert_data(sql)


