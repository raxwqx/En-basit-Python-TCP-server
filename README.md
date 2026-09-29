# 🐍 En Basit Python TCP Sunucusu

Kontrollü ortamlarda TCP bağlantılarını ve Python socket programlamayı öğrenmek için geliştirilmiş basit bir TCP sunucusudur.

## 🚀 Özellikler

- TCP bağlantılarını dinler
- Bağlanan istemcinin IP adresini gösterir
- İstemciye mesaj gönderir
- Python `socket` modülünü kullanır

## 📋 Kurulum

Python 3 gereklidir.

Python sürümünü kontrol etmek için:

```bash
python3 --version
```

## ▶️ Kullanım

Sunucuyu çalıştırmak için:

```bash
python3 server.py
```

Sunucu varsayılan olarak **8080** portunu dinler.

Örnek çıktı:

```text
[*] TCP Server başlatıldı: 0.0.0.0:8080
```

## 🧪 Test

Aynı bilgisayardan bağlantıyı test etmek için:

```bash
nc 127.0.0.1 8080
```

Bağlantı başarılı olduğunda sunucu istemciye şu mesajı gönderir:

```text
Hello from Python TCP Server!
```

## ⚠️ Yasal Uyarı

Bu proje eğitim amacıyla hazırlanmıştır.

Yalnızca kendi sistemlerinizde, CTF ortamlarında veya açıkça izin verilen kontrollü sistemlerde kullanılmalıdır.

İzinsiz sistemlere bağlantı kurmak veya tarama yapmak yasal ve etik sorunlara neden olabilir.

## 📚 Öğrenme Konuları

Bu proje aşağıdaki temel konuları öğrenmek için kullanılabilir:

- Python Socket Programming
- TCP/IP
- TCP bağlantıları
- Portlar
- Client/Server mimarisi
- Temel network security

## 📄 License

MIT License
