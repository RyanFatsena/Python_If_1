#Latihan1Chapter5
#3
indo = int(input('Nilai Bahasa Indonesia :'))
mtk = int(input('Nilai Matematika :'))
ipa = int(input('Nilai IPA:'))

print('==========================')

if(indo <= 0 or indo >= 100):
    print('Maaf input ada yang tidak valid')
elif(ipa <= 0 or ipa >= 100):
    print('Maaf input ada yang tidak valid')
elif (mtk <= 0 or mtk >= 100):
    print('Maaf input ada yang tidak valid')
    
elif(indo > 60 and ipa > 60 and mtk > 70):
    print ('Status kelulusan : Lulus')
else:
    print ('Status kelulusan : Tidak lulus')
    print('Sebab :')
    
    if(indo < 60):
        print('Nilai Bahasa Indonesia Kurang Dari 60')
    if(mtk < 70):
        print('Nilai Matematika Kurang Dari 70')