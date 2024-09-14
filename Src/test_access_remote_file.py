import skimage as ski
import matplotlib.pyplot as plt

#url = requests.get('https://drive.google.com/file/d/1-4-ZpLtFk_JoLc4CfdbQ4iUCtBGXKO9h/view?usp=drive_link')
image = ski.io.imread("https://montessori-rennes.org/rakuten/image_test/image_1000095714_product_345301179.jpg")


plt.imshow(image)
plt.show()

#df = pd.read_csv(csv_raw)


