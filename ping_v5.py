# dziala na 100%

format_str = input()
ile_str = input()
ile = int(ile_str)

znak_formatu = ''
for znak in format_str:
    if znak in ['.', '-', '/', ' ']:
        znak_formatu = znak

while ile > 0:  # Corrected loop condition
    tymczas = input()
    znak_tymczas = ''
    pierwszy = 0
    drugi = 0

    for i, znak in enumerate(tymczas):
        if znak in ['.', '/', '-', ' ']:
            znak_tymczas = znak
            tymczas = tymczas[:i] + znak_formatu + tymczas[i + 1:]
            if pierwszy == 0:
                pierwszy = i
            elif pierwszy != 0 and drugi == 0:
                drugi = i

    if znak_formatu == ' ' and znak_tymczas != ' ':
        miesiac = tymczas[pierwszy + 1:pierwszy + 3]
        miesiac_dict = {
            "01": "I", "02": "II", "03": "III", "04": "IV",
            "05": "V", "06": "VI", "07": "VII", "08": "VIII",
            "09": "IX", "10": "X", "11": "XI", "12": "XII"
        }
        if miesiac in miesiac_dict:
            miesiac = miesiac_dict[miesiac]
        tymczas = tymczas[:pierwszy + 1] + miesiac + tymczas[pierwszy + 3:]

    elif znak_formatu != ' ' and znak_tymczas == ' ':
        miesiac = tymczas[pierwszy + 1:drugi]
        miesiac_dict = {
            "I": "01", "II": "02", "III": "03", "IV": "04",
            "V": "05", "VI": "06", "VII": "07", "VIII": "08",
            "IX": "09", "X": "10", "XI": "11", "XII": "12"
        }
        if miesiac in miesiac_dict:
            miesiac = miesiac_dict[miesiac]
        tymczas = tymczas[:pierwszy + 1] + miesiac + tymczas[drugi:]

    print(tymczas)
    ile -= 1
