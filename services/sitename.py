from __future__ import division
import json

def lambda_handler(event, context):
    number1 = event['Number1']
    number2 = event['Number2']
    sum = number1 + number2
    product = number1 * number2
    difference = abs(number1 - number2)
    quotient = number1 / number2
    return {
        "number1": number1,
        "number2": number2,
        "sum": sum,
        "product": product,
        "quotient": quotient
    }
