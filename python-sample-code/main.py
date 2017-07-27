import tuna
import downLoadImage

downLoadImage.downLoadImage("https://thenewboston.com/photos/users/2/resized/869b40793dc9aa91a438b1eb6ceeaa96.jpg")

fw = open('simplr.txt', 'w')
fw.write('Learning python is cool.\n')
fw.write('too cool\n')
fw.close()

fr = open('simplr.txt', 'r')
text = fr.read()
print(text)
fr.close()



