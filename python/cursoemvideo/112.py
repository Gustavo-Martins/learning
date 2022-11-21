from packages.data.check import check
from packages.currency.currency import summary


price = check('Digite o preço: R$ ')
summary(price, 35, 22)
