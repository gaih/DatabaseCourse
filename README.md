# Global AI Hub - Veri Tabanı Eğitimi (21-22-23 Mart 2022)

![Logo](https://globalaihub.com/wp-content/uploads/2021/11/logo_quality_min.png)
## Veri Tabanı Eğitiminin 2. gününde kullanılan komutlar aşağıda sıralanmıştır. İyi çalışmalar!  
&nbsp;

1. 
    ```
    CREATE TABLE "bakkaldefter" ("isim" TEXT, "soyisim"	TEXT, "sokak"	TEXT, "odenecek_tutar"	INTEGER);
    ```

    Bu komut ile veri tabanında "bakkaldefter" isimli bir tablo oluşturuyoruz. Parentez içinde yazılı değerler sütunların isimleri ve bu sütunlardaki verilerin tipleri şeklinde olacak. Eklemek istediğimiz her bir sütun için virgülle ayırarak sütun ismi ve veri tipi girebiliriz.

&nbsp;

2. 
    ```
    INSERT INTO bakkaldefter VALUES("ALP", "SARICA", "Çiçek Sokak", "320");
    ```
    Komutu ile oluşturulan tabloya veri ekleyebiliriz.

    <br/>

    >Yukarıdaki 2 komut ile oluşturlan örnek tablo aşağıdaki gibi gözükecektir.

    |isim   |soyisim    |sokak  |odenecek tutar
    |--------|--------|--------|--------
    |Alp    |Sarıca     |Çiçek Sokak    |320
    |Gunel  |Aghakishiyeva  |Sevinç Sokak    |90
    |Ömer   |Cengiz     |Turgut Sokak    |178

&nbsp;

3. 
    ```
    SELECT * FROM bakkaldefter;
    ```

    Bu komut ile tablodaki bütün satırları görüntüleriz.

&nbsp;

4. 
    ```
    SELECT isim, soyisim FROM bakkaldefter WHERE odenecek_tutar > 300;
    ```

    Bu komut 300 liradan daha fazla borcu olan insanların isim ve soyisimlerini verecektir.

&nbsp;

5. 
    ```
    SELECT isim, soyisim FROM bakkaldefter WHERE odenecek_tutar >= 100 AND odenecek_tutar <300;
    ```

    Komutu, borcu 100 lira ile 300 lira arasında olan insanların isim ve soyisimlerini verecektir. Tam olarak 100 lira borcu olanlar sonuca dahile olacak fakat 300 lira borcu olanlar dahil olmayacaktır.

&nbsp;

6. 
    ```
    SELECT isim, soyisim FROM bakkaldefter ORDER BY odenecek_tutar DESC LIMIT 10;
    ```

    Bu komut odenecek_tutar sütununa göre değerleri azalan şekilde sıralayacak ve sadece ilk 10 satırı gösterecektir.

&nbsp;

7. 
    ```
    SELECT isim, soyisim FROM bakkaldefter ORDER BY odenecek_tutar ASC LIMIT 10;
    ```

    Bu komut odenecek_tutar sütununa göre değerleri artan şekilde sıralayacak ve sadece ilk 10 satırı gösterecektir.

&nbsp;

8. 
    ```
    SELECT DISTINCT sokak from bakkaldefter;
    ```

    Bu komut ile farklı sokak isimleri görüntülenecektir. Yani birden fazla satırda aynı sokak ismi varsa, ekrana o sokağın ismi sadece bir kere yazılacaktır.

&nbsp;

9. 
    ```
    UPDATE bakkaldefter SET sokak = "Borçlular Sokağı" WHERE sokak = "Sevinç Sokak";
    ```

    Bu komut ile tabloda sokak ismi "Sevinç Sokak" olan satırların sokak isimlerini "Borçlular Sokağı" olarak güncellenir.

&nbsp;

10. 
    ```
    DELETE from bakkaldefter WHERE isim = "Turgut";
    ```

    Bu komut ile tabloda ismi Turgut olan satırlar silinecektir.

&nbsp;

11. 
    ```
    DELETE from bakkaldefter WHERE sokak = "MFÖ" AND isim = "Mazhar";
    ```

    Bu komut ile MFÖ sokağında oturan Mazhar isimli satır silinecektir.
