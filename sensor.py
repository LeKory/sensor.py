import streamlit as st

car_simulation = {'gas_warning':1, 'speed_limit':100, 'temp_warning':30, '轉速':12000}
gas = int(input('油量的資料收集:油箱滿是10格 =>'))
speed= float(input('車速的資料收集:限速100 =>'))
temp = float(input('溫度的資料收集:限溫30 =>'))
轉速=int(input('轉速資料的收集:限轉12000 =>'))
confirm_input = st.button('請輸入確認')
if confirm_input:
  if gas <= car_simulation.get('gas_warning'):
    write('油箱只剩', gas, '格! 準備加油!!')
  else:
      write('油箱還剩', gas, '格。')
  if speed>=car_simulation.get('speed_limit'):
      writet('即將超速')
  else:
      write('安全')
  if temp>=car_simulation.get('temp_warning'):
      write('過熱')
  else:
      write('正常')
  if 轉速>=car_simulation.get('轉速'):
      write('即將超過轉速')
  else:
      write('正常')
