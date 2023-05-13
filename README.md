# Esthetic-women
Python program to Capture selfie using cv2 and match the skin color to nearest shades in shades.csv (dataset in kaggle that contains various Internationally recognised cosmetic brands and their foundation products with hex codes and hsv values).
Flow chart:
RUN CODE
   |
WEB CAM OPENS IN A GUI WITH BUTTON FOR TAKING PICTURES
   |
AFTER SNAPSHOT IS TAKEN LEFT MOUSE BUTTON CLUCKS OVER THE IMAGE SHOULD FETCH THE HSV VALUES (X,Y,Z) AND COMPARE THEM WITH ALL SHADES HSV VALUE IN THE DATASET AND RETURN THE CLOSESET MATCH
   |
THAT NEAREST/CLOSEST MATCHING SHADE SHOULD BE PRINTED AS 'BRAND_ NAME -PRODUCT-NAME'
