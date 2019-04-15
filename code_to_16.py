from arrays import DynamicArray


class Encoder:
    def convert(self, message):
        res_2 = 0
        new_arr = DynamicArray()
        for letter in message:
            res_1 = ord(letter) % 16
            angle = (res_1 - res_2) * 22.5
            if angle > 180:
                angle = -360 - angle
            if angle < -180:
                angle = 360 + angle


            # new_arr.append((res_1 - res_2) * 22.5)
            res_2 = ord(letter) // 16
            angle_2 = (res_2 - res_1) * 22.5
            if angle_2 > 180:
                angle_2 = -(360 - angle_2)
            if angle_2 < -180:
                angle_2 = 360 + angle_2
            new_arr.append(angle_2)
            new_arr.append(angle)
            print(res_2, res_1)
            # new_arr.append((res_2 - res_1) * 22.5)

            # new_arr.append((res_1, res_2))
        return new_arr


if __name__ == "__main__":
    mes = Encoder().convert("ABC")
    for i in range(len(mes)):
        print(mes[i])
