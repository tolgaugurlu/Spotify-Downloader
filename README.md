# Spootify Downloader

**Spootify Downloader**, Spotify çalma listelerindeki şarkıları YouTube'da bulur ve indirir - albüm kapakları, şarkı sözleri ve meta verileri ile birlikte.

> spotDL: En hızlı, en kolay ve en doğru komut satırı müzik indirme aracı.

</div>

---

## Kurulum

Daha fazla ayrıntı için [Kurulum Kılavuzuna](https://spotdl.rtfd.io/en/latest/installation/) başvurun.

### Python (Tavsiye Edilen Yöntem)

-   _spotDL_, `pip install spotdl` komutunu çalıştırarak yüklenebilir.
-   spotDL'yi güncellemek için `pip install --upgrade spotdl` komutunu çalıştırın.

> Bazı sistemlerde `pip` yerine `pip3` kullanmanız gerekebilir. (Örn: macOS)

<details>
    <summary style="font-size:1.25em"><strong>Diğer seçenekler</strong></summary>

-   Önceden derlenmiş yürütülebilir dosya
    -   En son sürümü [Yayınlar Sekmesinden](https://github.com/spotDL/spotify-downloader/releases) indirebilirsiniz.
-   Termux için
    -   `curl -L https://raw.githubusercontent.com/spotDL/spotify-downloader/master/scripts/termux.sh | sh` komutunu kullanabilirsiniz.
-   Arch
    -   spotDL için [Arch User Repository (AUR) paketi](https://aur.archlinux.org/packages/python-spotdl/) bulunmaktadır.
-   Docker

    -   Görüntüyü oluşturun:

        ```bash
        docker build -t spotdl .
        ```

    -   spotDL parametreleriyle birlikte bir konteyner başlatın (aşağıdaki bölüme bakın). Şarkı dosyalarına erişmek için eşlenmiş bir volume oluşturmanız gerekmektedir.

        ```bash
        docker run --rm -v $(pwd):/music spotdl download [trackUrl]
        ```

-   Kaynak koddan derleme
    ```bash
    git clone https://github.com/spotDL/spotify-downloader && cd spotify-downloader
    pip install poetry
    poetry install
    poetry run python3 scripts/build.py
    ```
    Oluşturulan yürütülebilir dosya `spotify-downloader/dist/` dizininde yer alır.

</details>

### FFmpeg Kurulumu

spotDL için FFmpeg gereklidir. FFmpeg'i yalnızca spotDL için kullanacaksanız, FFmpeg'i spotDL kurulum dizinine yüklemeniz yeterlidir:
`spotdl --download-ffmpeg`

Yukarıdaki seçeneği öneririz, ancak FFmpeg'i sisteminize genel olarak yüklemek isterseniz, aşağıdaki talimatları izleyin.

-   [Windows Kılavuzu](https://windowsloop.com/install-ffmpeg-windows-10/)
-   OSX - `brew install ffmpeg`
-   Linux - `sudo apt install ffmpeg` veya dağıtımınızın paket yöneticisini kullanın

## Kullanım

Seçeneksiz olarak SpotDL'yi kullanmak::

```sh
spotdl [urls]

spootdl yazdıktan sonra linki yapıştırmanız yeterli.
```

Eğer komut satırında çalıştırmakta sorun yaşıyorsanız, spotDL'yi bir paket olarak çalıştırabilirsiniz:

```sh
python -m spotdl [urls]
```

Genel kullanım:

```sh
spotdl [operation] [options] QUERY
```

spotDL'nin gerçekleştirebileceği farklı **operation** (işlemler) bulunmaktadır. Varsayılanı `download` olan işlem, şarkıları YouTube'dan indirir ve meta verileriyle birlikte gömülür.

spotDL için **query** genellikle Spotify URL'lerinin bir listesidir, ancak **sync** gibi bazı işlemler için yalnızca tek bir bağlantı veya dosya gereklidir.
Tüm **options** seçenekleri için `spotdl -h` komutunu kullanın.

<details>
<summary style="font-size:1em"><strong>Desteklenen işlemler</strong></summary>

-   `save`: Spotify'dan sadece meta verileri kaydeder ve hiçbir şey indirmez.

    -   Kullanım:
        `spotdl save [query] --save-file {filename}.spotdl`

-   `web`: Komut satırı yerine web arayüzünü başlatır. Ancak sınırlı özelliklere sahiptir ve yalnızca tek şarkı indirmeyi destekler.

-   `url`: Sorgudaki her şarkı için doğrudan indirme bağlantısını alır.

    -   Kullanım:
        `spotdl url [query]`

-   `sync`: Dizinleri günceller. Dizini mevcut çalma listesi durumuyla karşılaştırır. Yeni eklenen şarkılar indirilir ve silinen şarkılar silinir. Başka şarkılar indirilmez ve başka dosyalar silinmez.

    -   Kullanım:
        `spotdl sync [query] --save-file {filename}.spotdl`

        Bu, yeni bir **sync** dosyası oluşturur, dizini gelecekte güncellemek için şunu kullanın:

        `spotdl sync {filename}.spotdl`

-   `meta`: Sağlanan şarkı dosyalarının meta verilerini günceller.
</details>

## Müzik Kaynakları ve Ses Kalitesi

spotDL, müzik indirmek için YouTube'u bir kaynak olarak kullanır. Bu yöntem, Spotify üzerinden müzik indirme ile ilgili herhangi bir sorunun önlenmesi için kullanılır.

> **Not**
> Kullanıcılar kendi eylemlerinden ve olası yasal sonuçlardan sorumludur. Telif hakkıyla korunan materyallerin izinsiz indirilmesini desteklemiyoruz ve kullanıcı eylemlerinden sorumlu değiliz.

### Ses Kalitesi

spotDL, müziği YouTube'dan indirir ve her zaman en yüksek mümkün olan bit hızını indirir. Bu, düzenli kullanıcılar için 128 kbps ve YouTube Music premium kullanıcıları için 256 kbps'dir.

Daha fazla bilgi için [Audio Formats](docs/usage.md#audio-formats-and-quality) sayfasına bakın.
