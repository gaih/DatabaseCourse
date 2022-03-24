# Global AI Hub - Veri Tabanı Eğitimi

<div align="center">
    <img src="logo.png">
</div>

<div align="center">
    <p>Veri Tabanı Eğitiminin 2. gününde kullanılan komutlar aşağıda sıralanmıştır. İyi çalışmalar!</p>
</div>

---
1. 
    ```
    CREATE TABLE "bakkaldefter" ("isim" TEXT, "soyisim"	TEXT, "sokak"	TEXT, "odenecek_tutar"	INTEGER);
    ```

    >Bu komut ile veri tabanında "bakkaldefter" isimli bir tablo oluşturuyoruz. Parentez içinde yazılı değerler, sütunların isimleri ve bu sütunlardaki verilerin tipleri şeklinde olacak. Eklemek istediğimiz her bir sütun için virgülle ayırarak sütun ismi ve veri tipi girebiliriz.

&nbsp;

2. 
    ```
    INSERT INTO bakkaldefter VALUES("ALP", "SARICA", "Çiçek Sokak", "320");
    ```

    >Komutu ile oluşturulan tabloya veri ekleyebiliriz.

&nbsp;

3. 
    ```
    SELECT * FROM bakkaldefter;
    ```

    >Bu komut ile tablodaki bütün satırları görüntüleriz.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Alp    |Sarıca     |Çiçek Sokak    |320
    |Gunel  |Aghakishiyeva  |Sevinç Sokak    |90
    |Ömer   |Cengiz     |Turgut Sokak    |178
    |Ali    |Desidero     |MFÖ    |78
    |Mazhar  |Alanson  |MFÖ    |969
    |Zeynep   |Hayal     |Meriç Sokak    |745

&nbsp;

4. 
    ```
    SELECT isim, soyisim FROM bakkaldefter WHERE odenecek_tutar > 300;
    ```

    >Bu komut 300 liradan daha fazla borcu olan insanların isim ve soyisimlerini verecektir.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Alp    |Sarıca     |Çiçek Sokak    |320
    |Mazhar  |Alanson  |MFÖ    |969
    |Zeynep   |Hayal     |Meriç Sokak    |745

&nbsp;

5. 
    ```
    SELECT isim, soyisim FROM bakkaldefter WHERE odenecek_tutar >= 100 AND odenecek_tutar <300;
    ```

    >Komutu, borcu 100 lira ile 300 lira arasında olan insanların isim ve soyisimlerini verecektir. Tam olarak 100 lira borcu olanlar sonuca dahile olacak fakat 300 lira borcu olanlar dahil olmayacaktır.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Ömer   |Cengiz     |Turgut Sokak    |178

&nbsp;

6. 
    ```
    SELECT isim, soyisim FROM bakkaldefter ORDER BY odenecek_tutar DESC LIMIT 4;
    ```

    >Bu komut odenecek_tutar sütununa göre değerleri azalan şekilde sıralayacak ve sadece ilk 4 satırı gösterecektir.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Mazhar  |Alanson  |MFÖ    |969
    |Zeynep   |Hayal     |Meriç Sokak    |745
    |Alp    |Sarıca     |Çiçek Sokak    |320
    |Ömer   |Cengiz     |Turgut Sokak    |178

&nbsp;

7. 
    ```
    SELECT isim, soyisim FROM bakkaldefter ORDER BY odenecek_tutar ASC LIMIT 4;
    ```

    >Bu komut odenecek_tutar sütununa göre değerleri artan şekilde sıralayacak ve sadece ilk 4 satırı gösterecektir.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Ali    |Desidero     |MFÖ    |78
    |Gunel  |Aghakishiyeva  |Sevinç Sokak    |90
    |Ömer   |Cengiz     |Turgut Sokak    |178
    |Alp    |Sarıca     |Çiçek Sokak    |320

&nbsp;

8. 
    ```
    SELECT DISTINCT sokak from bakkaldefter;
    ```

    >Bu komut ile farklı sokak isimleri görüntülenecektir. Yani birden fazla satırda aynı sokak ismi varsa, ekrana o sokağın ismi sadece bir kere yazılacaktır.

    |sokak
    |--------
    |Sevinç Sokak
    |Turgut Sokak
    |MFÖ
    |Meriç Sokak

&nbsp;

9. 
    ```
    UPDATE bakkaldefter SET sokak = "Borçlular Sokağı" WHERE sokak = "Sevinç Sokak";
    ```

    >Bu komut ile tabloda sokak ismi "Sevinç Sokak" olan satırların sokak isimlerini "Borçlular Sokağı" olarak güncellenir.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Alp    |Sarıca     |Çiçek Sokak    |320
    |Gunel  |Aghakishiyeva  |Borçlular Sokağı    |90
    |Ömer   |Cengiz     |Turgut Sokak    |178
    |Ali    |Desidero     |MFÖ    |78
    |Mazhar  |Alanson  |MFÖ    |969
    |Zeynep   |Hayal     |Meriç Sokak    |745

&nbsp;

10. 
    ```
    DELETE from bakkaldefter WHERE sokak = "MFÖ" AND isim = "Mazhar";
    ```

    >Bu komut ile MFÖ sokağında oturan Mazhar isimli satır silinecektir.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Alp    |Sarıca     |Çiçek Sokak    |320
    |Gunel  |Aghakishiyeva  |Borçlular Sokağı    |90
    |Ömer   |Cengiz     |Turgut Sokak    |178
    |Ali  |Desidero  |MFÖ    |78
    |Zeynep   |Hayal     |Meriç Sokak    |745

&nbsp;

11. 
    ```
    DELETE from bakkaldefter WHERE isim = "Ali";
    ```

    >Bu komut ile tabloda ismi Turgut olan satırlar silinecektir.

    |isim   |soyisim    |sokak  |odenecek_tutar
    |--------|--------|--------|--------
    |Alp    |Sarıca     |Çiçek Sokak    |320
    |Gunel  |Aghakishiyeva  |Borçlular Sokağı    |90
    |Ömer   |Cengiz     |Turgut Sokak    |178
    |Zeynep   |Hayal     |Meriç Sokak    |745

