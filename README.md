# Newest Indonesia Earthquake
This package will get the newest earthquake from BMKG | Meteorological, Climatological, and Geophysical Agency.

## How it work?
This package will scrape from [BMKG](https://bmkg.go.id) to get newest quake happened in Indonesia.

It package will use BeautifulSoup4 and Request,to produce output in the form of JSON that is ready to be used in web or mobile applications

## How To Use!
```
import  gempaterbaru

if __name__ == '__main__':
    print("Aplikasi utama")
    result = gempaterbaru.ekstrasi_data()
    gempaterbaru.tampilkan_data(result)
```
### Author
Deni Rahmawan