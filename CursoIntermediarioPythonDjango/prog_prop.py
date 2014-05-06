class Forno(object):
  def __init__(self):
    self._temp = 0

  def _get_temp(self):
    return self._temp

  def _set_temp(self, temp):
    if temp > 250:
      raise ValueError("Maxima: 250")
    self._temp = temp

  temp = property(_get_temp,
                  _set_temp)

forno = Forno()
print forno.temp # 0

forno.temp = 120
print forno.temp # 120

forno.temp = 300 # ValueError
