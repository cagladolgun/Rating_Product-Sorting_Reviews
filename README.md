Amazon Ürün Puanlama ve Yorum Sıralama Projesi

Bu proje, Amazon ürün verilerini kullanarak ürünlerin puanlaması ve yorumlarının sıralanmasına yönelik bir analiz içerir. Projede, ürünlerin ortalama puanları hesaplanmış ve tarihe göre ağırlıklı ortalama puanları karşılaştırılmıştır. Ayrıca, en faydalı 20 yorumu belirlemek için farklı yöntemler uygulanmıştır.

Amaç

E-ticaret dünyasında ürünlere verilen puanların ve yorumların doğru bir şekilde sıralanması, hem müşteri memnuniyetini artırmak hem de satıcıların satışlarını optimize etmek için büyük önem taşır. Bu proje, Amazon'daki ürünlerin puanlamalarını doğru şekilde değerlendirmeyi ve yorumların sıralanmasında daha adil bir yöntem geliştirmeyi amaçlamaktadır.

Veri Seti

Veri seti Amazon'dan alınan kullanıcı puanları ve yorumlardan oluşmaktadır. Elektronik kategorisindeki en fazla yorum alan ürünün kullanıcı verilerini içermektedir.

Değişken Sayısı: 12

Gözlem Sayısı: 4915

Veri Seti Boyutu: 71.9 MB

Değişkenler:

reviewerID: Kullanıcı ID’si

asin: Ürün ID’si

reviewerName: Kullanıcı Adı

helpful: Faydalı değerlendirme derecesi

reviewText: Değerlendirme metni

overall: Ürün puanı

summary: Değerlendirme özeti

unixReviewTime: Unix değerlendirme zamanı

reviewTime: Değerlendirme zamanı

day_diff: Değerlendirmeden itibaren geçen gün sayısı

helpful_yes: Faydalı bulunma sayısı

total_vote: Toplam oy sayısı

Proje Görevleri

Görev 1: Ürün Puanlaması

Ürünün ortalama puanı hesaplanmıştır.

Tarihe göre ağırlıklı ortalama puan hesaplanmış ve karşılaştırılmıştır.

Zaman dilimlerine göre farklı puan ortalamaları yorumlanmıştır.

Görev 2: Yorumların Sıralanması

helpful_no değişkeni üretilmiştir.

score_pos_neg_diff, score_average_rating ve wilson_lower_bound skorları hesaplanarak veri setine eklenmiştir.

En faydalı 20 yorum bu skorlara göre belirlenmiştir.

Kullanılan Yöntemler

Ağırlıklı Ortalama: Verilen değerlendirmelerin zamana göre ağırlıklandırılması.

Wilson Lower Bound Skoru: Yorumların güvenilirliğine göre sıralanmasını sağlayan istatistiksel bir yöntem.
Pos-Negatif Farkı: Faydalı bulunan ve bulunmayan oylar arasındaki farkı kullanarak sıralama yapılması.
Sonuçlar
Proje kapsamında hesaplanan ağırlıklı ortalama puanlar, zaman geçtikçe yorumların puanlamalara nasıl etki ettiğini göstermektedir. Ayrıca, yorum sıralamasında Wilson Lower Bound yöntemi kullanılarak en güvenilir ve faydalı yorumların öne çıkarılması sağlanmıştır.
