from arrays import DynamicArray


class Encoder:
    def convert(self, message):
        arr = DynamicArray()
        for letter in message:
            res_2 = ord(letter) % 16
            res_1 = ord(letter) // 16
            arr.append(res_1)
            arr.append(res_2)
        angle = 0
        result = DynamicArray()
        for i in range(len(arr)):
            angle_turn = arr[i] * 22.5 - angle
            angle += angle_turn
            result.append(angle_turn)
        return result


if __name__ == "__main__":
    mes = Encoder().convert("ABCDEFGHIJKLMNOP")
    for i in range(len(mes)):
        print(mes[i])

