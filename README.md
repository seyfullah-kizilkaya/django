# E-Ticaret Platformu

Bu proje, Django framework'ü kullanarak geliştirilmiş bir **e-ticaret platformudur**. Kullanıcılar için güvenli bir alışveriş deneyimi sunan bu platformda aşağıdaki özellikler bulunmaktadır:

## Temel Özellikler

- **Ürün Yönetimi**: Admin panelinden ürünler ve kategoriler kolayca yönetilebilir.
- **Ödeme Entegrasyonu**: Güvenli ödeme işlemleri için entegrasyon sağlanmıştır.
- **Kullanıcı Kaydı ve Kimlik Doğrulama**: Kullanıcıların hesap yönetimi güvenli bir şekilde yapılır.

## Diğer Özellikler

- Yüksek performanslı ürün kataloğu ile hızlı ve verimli arama.
- Güçlü güvenlik önlemleri sayesinde kullanıcı verileri korunur.
- Ölçeklenebilir altyapı ile platform büyüdükçe performans kaybı yaşanmaz.

## Kurulum

Projenin çalışabilmesi için aşağıdaki adımları izleyebilirsiniz:

1. Depoyu klonlayın:
    ```bash
    git clone https://github.com/seyfullah-kizilkaya/django.git
    ```

2. Gereksinimleri yüklemek için:
    ```bash
    pip install -r requirements.txt
    ```

3. Veritabanını yapılandırın:
    ```bash
    python manage.py migrate
    ```

4. Geliştirme sunucusunu çalıştırın:
    ```bash
    python manage.py runserver
    ```

## Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır.
