from __future__ import division
import json

def lambda_handler(event, context):
    number1 = event['Number1']
    number2 = event['Number2']
    my_sum = number1 + number2
    product = number1 * number2
    difference = abs(number1 - number2)
    quotient = 'NaN' if number2 == 0 else number1 / number2
    return {
        "number1": number1,
        "number2": number2,
        "sum": my_sum,
        "product": product,
        "quotient": quotient
    }
