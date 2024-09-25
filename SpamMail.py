import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Spam mesajları ve ham mesajları burada tanımlayın
spam_messages = [
    "Kazandınız! Hemen ödülünüzü talep edin!"
"Şanslısınız! Bir hediye kazanma şansınız var!"
"Para kazanmak için hemen kaydolun!"
"İlk yatırımınıza %100 bonus kazanın!"
"Hızla büyüyen bir şirkete katılın ve zenginleşin!"
"İçeride sizi bekleyen fırsatları kaçırmayın!"
"Özel teklif: İlk 100 kişiye ücretsiz deneme!"
"Kumar oynayarak hızlı para kazanma yöntemleri!"
"Bu fırsat sadece sınırlı bir süre için geçerli!"
"Bugün kaydolursanız, ekstra bonus alacaksınız!"
"Kumarhane bonusunu kaçırmayın!"
"Üç kat bonus kazanın! Şimdi katılın!"
"Hızla kazanın! Hemen tıklayın!"
"Yalnızca size özel indirim kuponları!"
"Yeni bir yatırım fırsatı ile karşınızdayız!"
"Bu e-posta size özel fırsatlar sunuyor!"
"Bugün tıklarsanız büyük bir ödül kazanabilirsiniz!"
"Bağış yapın, karşılığında büyük ödüller kazanın!"
"Özel teklif: Arkadaşınızı davet edin, bonus kazanın!"
"Hemen kaydolun, büyük ikramiyeyi kazanın!"
"Bu fırsat kaçmaz! Hemen katılın!"
"Yüzde 50 indirim fırsatı sizi bekliyor!"
"Şimdi kaydolun, bir arkadaşınıza da bonus kazandırın!"
"Kazancınızı artırmanın en kolay yolu!"
"Bugün sadece sizin için %20 indirim!"
"Ücretsiz ürün almak için tıklayın!"
"Sadece bugün geçerli özel teklifler!"
"Ödül programımıza katılın ve kazanın!"
"Siz de hemen kaydolun, kazanmanın keyfini çıkarın!"
"Yeni kazanç fırsatlarıyla tanışın!"
"Para kazanmanın kolay yolu burada!"
"Bir arkadaşınıza önerin, bonus kazanın!"
"Hediye çekleri kazanmak için hemen kaydolun!"
"Sizi bekleyen fırsatlarla dolu bir e-posta!"
"Son dakika fırsatları! Hemen inceleyin!"
"Para kazanmak için doğru yerdesiniz!"
"Kazancınızı artırmanın en kolay yolu!"
"Sadece birkaç tıklama ile kazanabilirsiniz!"
"Yüksek kazanç fırsatlarıyla dolu bir yatırım!"
"İçeride özel teklifler var! Kaçırmayın!"
"Bugün kaydolursanız büyük bir indirim kazanabilirsiniz!"
"Yüzde 70 indirim fırsatını kaçırmayın!"
"Ödüller kazanmak için tıklayın!"
"Bu mesaj sadece size özel!"
"Yeni yatırım fırsatları sizi bekliyor!"
"Zengin olmanın sırlarını keşfedin!"
"Yeni bir hesap açın, bonus kazanın!"
"Sadece birkaç dakika ayırarak kazanabilirsiniz!"
"Yatırım fırsatlarını kaçırmayın!"
"Bu mesaj sizi özel fırsatlarla karşılıyor!"
"Hızla büyüyen bir iş fırsatı!"
"Bugün kaydolursanız büyük kazançlar elde edebilirsiniz!"
"Yüzde 50 indirim fırsatı burada!"
"Ücretsiz hediyeler kazanmak için hemen kaydolun!"
"Bu fırsat kaçmaz! Hızla katılın!"
"Özel teklifler ve hediyeler sizi bekliyor!"
"Bir arkadaşınızı davet edin, büyük ödüller kazanın!"
"Bugün sadece sizin için geçerli indirimler!"
"Kazanç fırsatlarını kaçırmayın!"
"Zenginliğin kapısını aralayın!"
"Kumarhane bonuslarını kaçırmayın!"
"Yatırım yapın, kazancınızı artırın!"
"Bu mesajı görmenizin bir nedeni var: Kazanın!"
"Şimdi kaydolun, büyük ikramiyeyi kapın!"
"Bugün tıklarsanız ödüller kazanabilirsiniz!"
"Bir hediye kazanma şansınızı kaçırmayın!"
"Yatırım fırsatlarına göz atın!"
"Bu e-posta sadece sizin için hazırlandı!"
"Ücretsiz ürünler kazanmak için tıklayın!"
"Özel teklif: Bugün kaydolursanız bonus kazanırsınız!"
"Kazançlarınızı artırmanın en kolay yolu!"
"Hızla kazanın! Hemen tıklayın!"
"Yeni fırsatlarla dolu bir dünyaya adım atın!"
"Bu e-posta, sizi büyük fırsatlarla karşılıyor!"
"Ödüller kazanmak için hemen kaydolun!"
"Şansınız yaver gitti! Kazanın!"
"Bu fırsat sadece sizler için geçerli!"
"Kumar oynayarak zenginleşmenin yolları!"
"Bu e-posta sadece sizin için hazırlanmıştır!"
"Özel indirimlerden yararlanın!"
"Bugün tıklayın, büyük kazançlar elde edin!"
"Yüzde 80 indirim fırsatını kaçırmayın!"
"Yeni ürünler, yeni kazanç fırsatları!"
"Bir arkadaşınıza önerin, ekstra kazançlar elde edin!"
"İçeride sizi bekleyen büyük fırsatlar var!"
"Zenginliğe giden yol burada başlıyor!"
"Kazancınızı artırmak için doğru adrestesiniz!"
"Bugün kaydolursanız büyük ödüller kazanabilirsiniz!"
"Şanslısınız! Bu e-posta özel fırsatlar sunuyor!"
"Para kazanmak için hemen tıklayın!"
"Yüzde 50 indirim fırsatını kaçırmayın!"
"Bu mesajda büyük fırsatlar sizi bekliyor!"
"Özel teklifler ve bonuslar için kaydolun!"
"Kumarhaneye katılın, kazançlarınızı artırın!"
"Bu fırsatları kaçırmayın!"
"Ücretsiz ürün almak için hemen kaydolun!"
"Zengin olmanın sırlarını keşfedin!"
"Bugün kaydolun, büyük kazançların kapısını aralayın!"
"Ödül kazanmak için tıklayın!"
"Kazancınızı artırmanın en kolay yolu burada!"
"Şansınızı denemek için hemen kaydolun!"
"Bu mesaj sadece sizin için hazırlandı!"
"Özel teklifler ve indirimler sizi bekliyor!"
"Kumar oynamak için doğru yerdesiniz!"
"Hızla kazanın! Hemen katılın!"
"Yeni fırsatlarla dolu bir dünyaya adım atın!"
"Bu e-posta, sizi büyük kazançlarla buluşturacak!"
"Şimdi kaydolun, büyük ikramiyeyi kapın!"
"Kazancınızı artırmanın yollarını keşfedin!"
"Ödüller kazanmak için tıklayın!"
"Bu mesaj sadece size özel fırsatlar sunuyor!"
"Kumarhane bonuslarını kaçırmayın!"
"Bu fırsat kaçmaz! Hızla katılın!"
"Özel teklif: Bugün kaydolursanız ekstra kazançlar kazanırsınız!"
"Yüzde 50 indirim fırsatını kaçırmayın!"
"Bu mesajda büyük fırsatlar sizi bekliyor!"
"Özel teklifler ve bonuslar için kaydolun!"
"Kumarhaneye katılın, kazançlarınızı artırın!"
"Bu fırsatları kaçırmayın!"
"Ücretsiz ürün almak için hemen kaydolun!"
"Zengin olmanın sırlarını keşfedin!"
"Bugün kaydolun, büyük kazançların kapısını aralayın!"
"Ödül kazanmak için tıklayın!"
"Kazancınızı artırmanın en kolay yolu burada!"
"Şansınızı denemek için hemen kaydolun!"
"Bu mesaj sadece sizin için hazırlandı!"
"Özel teklifler ve indirimler sizi bekliyor!"
"Kumar oynamak için doğru yerdesiniz!"
"Hızla kazanın! Hemen katılın!"
"Yeni fırsatlarla dolu bir dünyaya adım atın!"
"Bu e-posta, sizi büyük kazançlarla buluşturacak!"
"Şimdi kaydolun, büyük ikramiyeyi kapın!"
"Kazancınızı artırmanın yollarını keşfedin!"
"Ödüller kazanmak için tıklayın!"
"Bu mesaj sadece size özel fırsatlar sunuyor!"
"Kumarhane bonuslarını kaçırmayın!"
"Bu fırsat kaçmaz! Hızla katılın!"
"Özel teklif: Bugün kaydolursanız ekstra kazançlar kazanırsınız!"
"Yüzde 50 indirim fırsatını kaçırmayın!"
"Bu mesajda büyük fırsatlar sizi bekliyor!"
"Özel teklifler ve bonuslar için kaydolun!"
"Kumarhaneye katılın, kazançlarınızı artırın!"
"Bu fırsatları kaçırmayın!"
"Ücretsiz ürün almak için hemen kaydolun!"
"Zengin olmanın sırlarını keşfedin!"
"Bugün kaydolun, büyük kazançların kapısını aralayın!"
"Ödül kazanmak için tıklayın!"
"Kazancınızı artırmanın en kolay yolu burada!"
"Şansınızı denemek için hemen kaydolun!"
"Bu mesaj sadece sizin için hazırlandı!"
"Özel teklifler ve indirimler sizi bekliyor!"
    "Kumar oynamak için doğru yerdesiniz!"
    "Hızla kazanın! Hemen katılın!"
    "Yeni fırsatlarla dolu bir dünyaya adım atın!"
    "Bu e-posta, sizi büyük kazançlarla buluşturacak!"
    "Şimdi kaydolun, büyük ikramiyeyi kapın!"
    "Hızla zenginleşmek ister misiniz? Hemen katılın!",
    "Sadece bu hafta sonu %100 bonus fırsatı!",
    "Şansını dene! Büyük ödüller seni bekliyor.",
    "Canlı bahislerde %50 indirim!",
    "Hızlı para kazanmanın yolu burada! Katıl!",
    "Tüm yeni üyeler için bedava bahis!",
    "Kumarhanemizde seni bekleyen büyük ödüller var!",
    "Yüzlerce oyun ve büyük kazanç fırsatları!",
    "Hemen kaydol, ücretsiz oyun oyna!",
    "Hızlı kazançlar için hemen kaydol!",
    "Kumarhane bonuslarımızdan yararlan!",
    "Şans oyunlarımızda kazanan sen olabilirsin!",
    "Sadece yeni üyeler için özel promosyon!",
    "Yüksek bahisler için hemen katıl!",
    "Sadece bugüne özel %200 bonus!",
    "Şimdi katıl, bedava para kazan!",
    "Kumarhane oyunlarında kazanan sensin!",
    "Büyük kazanç için hemen kaydol!",
    "Yüzde 50 kazanç artışı garantisi!",
    "Ücretsiz bahis fırsatlarını kaçırmayın!",
    "Sadece bu ay, büyük ikramiyeler!",
    "Tüm oyunlarda %75 indirim fırsatı!",
    "Hızla kazanmak için şimdi katıl!",
    "Bedava spin fırsatları seni bekliyor!",
    "Kumarhanemizde sadece seni bekliyoruz!",
    "Şimdi katıl, bedava bahislere sahip ol!",
    "Zenginlik kapıları aralanıyor, hemen tıkla!",
    "Büyük kazanç için hemen kaydol!",
    "Şans oyunlarımızda seni bekliyoruz!",
    "Hızla kazanmak için şimdi katıl!",
    "Göz alıcı ödüller seni bekliyor!",
    "Kumarhane bonuslarını kaçırma!",
    "Büyük kazançlar için katılma fırsatını yakala!",
    "Hızla kazan, hemen kaydol!",
    "Sadece bu hafta %100 bonus!",
    "Kumarhane oyunlarında büyük ödüller seni bekliyor!",
    "Kazandığınız her şey %100 bonusla!",
    "Yüzde 50 kazanç artışı garantisi!",
    "Ücretsiz bahis fırsatlarını kaçırmayın!",
    "Büyük kazançlar için kaydol!",
    "Yüzlerce oyun seni bekliyor!",
    "Hızla zenginleşmek için hemen kaydol!",
    "Hızlı kazanç sağlamak için kaydol!",
    "Sadece bu ay %30 indirimli ürünler!",
    "Hızla alışveriş yap, büyük tasarruf et!",
    "Sadece yeni müşterilere özel %25 indirim!",
    "Alışverişte %50'ye varan indirim fırsatları!",
    "Yüzlerce üründe büyük fırsatlar!",
    "Sınırlı süreli kampanyalar için hemen kaydol!",
    "Kaçırılmayacak fırsatlar seni bekliyor!",
    "Ücretsiz deneme fırsatları için hemen tıklayın!",
    "Yeni gelen ürünlerde büyük indirim!",
    "Alışverişte kazanan sen ol!",
    "Son dakika fırsatlarını kaçırmayın!",
    "Tüm ürünlerde %50 indirim!",
    "Hızlı ve kolay alışveriş için hemen tıklayın!",
    "İhtiyacınız olan her şey burada! Hemen tıklayın.",
    "Sadece bugün %30 indirimli ürünler!",
    "Son dakika! Hesabınıza para yatırdık, hemen kontrol edin!",
    "Yüzlerce üründe sınırlı süreli fırsatlar!",
    "Sadece bugüne özel %200 bonus!",
    "Alışverişte büyük fırsatlar seni bekliyor!",
    "Sınırlı süreli indirimler seni bekliyor!",
    "Yeni sezon ürünlerinde büyük indirim!",
    "Alışverişte kazanan sen ol!",
    "Hızla kapınıza gelen fırsatlar!",
    "Yüzlerce üründe büyük fırsatlar!",
    "İhtiyacınız olan her şey burada!",
    "Sınırlı süreli kampanyalar için hemen kaydol!",
    "Alışverişte %60'a varan indirim fırsatları!",
    "Sadece yeni müşterilere özel %25 indirim!",
    "Alışverişte büyük fırsatlar seni bekliyor!",
    "Tüm ürünlerde bedava kargo fırsatı!",
    "Yeni sezon ürünlerinde büyük indirim!",
    "Hızla alışveriş yap, büyük tasarruf et!",
    "Son dakika kampanyalarından yararlan!",
    "Alışverişte %50'ye varan indirim fırsatları!",
    "İhtiyacınız olan her şey burada!",
    "Yüzlerce üründe büyük fırsatlar!",
    "Hızla kapınıza gelen fırsatlar!",
    "Sınırlı süreli indirimler seni bekliyor!",
    "Kaçırılmayacak fırsatlar seni bekliyor!",
    "Ücretsiz deneme fırsatları için hemen tıklayın!",
    "Alışverişte kazanan sen ol!",
    "Son dakika fırsatlarını kaçırmayın!",
    "Hızla kazanmak için hemen kaydol!",
    "Büyük ödüller seni bekliyor!",
    "Son dakika! Hesabınıza para yatırdık, hemen kontrol edin!",
    "Yüzlerce üründe sınırlı süreli fırsatlar!",
    "Alışverişte kazanan sen ol!",
    "Ücretsiz deneme fırsatları için hemen tıklayın!",
    "İhtiyacınız olan her şey burada! Hemen tıklayın.",
    "Sadece yeni müşterilere özel %25 indirim!",
    "Hızla zenginleşmek ister misiniz? Hemen katılın!",
    "Sadece bu hafta sonu %100 bonus fırsatı!",
    "Hızlı para kazanmanın yolu burada! Katıl!",
    "Tüm yeni üyeler için bedava bahis!",
    "Kumarhanemizde seni bekleyen büyük ödüller var!",
    "Yüzlerce oyun ve büyük kazanç fırsatları!",
    "Hemen kaydol, ücretsiz oyun oyna!",
    "Hızlı kazançlar için hemen kaydol!",
    "Kumarhane bonuslarımızdan yararlan!",
    "Şans oyunlarımızda kazanan sen olabilirsin!",
    "Sadece yeni üyeler için özel promosyon!",
    "Yüksek bahisler için hemen katıl!",
    "Sadece bugüne özel %200 bonus!",
    "Şimdi katıl, bedava para kazan!",
    "Kumarhane oyunlarında kazanan sensin!",
    "Büyük kazanç için hemen kaydol!",
    "Yüzde 50 kazanç artışı garantisi!",
    "Ücretsiz bahis fırsatlarını kaçırmayın!",
    "Sadece bu ay, büyük ikramiyeler!",
    "Tüm oyunlarda %75 indirim fırsatı!",
    "Hızla kazanmak için şimdi katıl!",
    "Bedava spin fırsatları seni bekliyor!",
    "Kumarhanemizde sadece seni bekliyoruz!",
    "Şimdi katıl, bedava bahislere sahip ol!",
    "Zenginlik kapıları aralanıyor, hemen tıkla!",
    "Büyük kazanç için hemen kaydol!",
    "Şans oyunlarımızda seni bekliyoruz!",
    "Hızla kazanmak için şimdi katıl!",
    "Göz alıcı ödüller seni bekliyor!",
    "Kumarhane bonuslarını kaçırma!",
    "Büyük kazançlar için katılma fırsatını yakala!",
    "Hızla kazan, hemen kaydol!",
    "Sadece bu hafta %100 bonus!",
    "Kumarhane oyunlarında büyük ödüller seni bekliyor!",
    "Kazandığınız her şey %100 bonusla!",
    "Yüzde 50 kazanç artışı garantisi!",
    "Ücretsiz bahis fırsatlarını kaçırmayın!",
    "Büyük kazançlar için kaydol!",
    "Yüzlerce oyun seni bekliyor!",
    "Hızla zenginleşmek için hemen kaydol!",
    "Hızlı kazanç sağlamak için kaydol!",
    "Sadece bu ay %30 indirimli ürünler!",
    "Hızla alışveriş yap, büyük tasarruf et!",
    "Sadece yeni müşterilere özel %25 indirim!",
    "Alışverişte %50'ye varan indirim fırsatları!",
    "Yüzlerce üründe büyük fırsatlar!",
    "Sınırlı süreli kampanyalar için hemen kaydol!",
    "Kaçırılmayacak fırsatlar seni bekliyor!",
    "Ücretsiz deneme fırsatları için hemen tıklayın!",
    "Yeni gelen ürünlerde büyük indirim!",
    "Alışverişte kazanan sen ol!",
    "Son dakika fırsatlarını kaçırmayın!",
    "Tüm ürünlerde %50 indirim!",
    "Hızlı ve kolay alışveriş için hemen tıklayın!",
    "İhtiyacınız olan her şey burada!"
]
class SpamDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spam Tespit Uygulaması")
        
        # Pencere boyutunu büyütün
        self.root.geometry("800x600")
        
        # Merkezleme işlemi
        self.center_window()
        
        self.label = tk.Label(root, text="Mesajınızı girin:")
        self.label.pack(pady=10)

        self.text_input = tk.Text(root, height=5, width=40)
        self.text_input.pack(pady=10)

        self.check_button = tk.Button(root, text="Kontrol Et", command=self.check_spam)
        self.check_button.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

    def center_window(self):
        width = self.root.winfo_reqwidth()
        height = self.root.winfo_reqheight()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def check_spam(self):
        user_input = self.text_input.get("1.0", tk.END).strip()
        if not user_input:
            messagebox.showwarning("Uyarı", "Lütfen bir mesaj girin.")
            return

        # TF-IDF vektörleştirme
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(spam_messages + [user_input])
        cosine_sim = cosine_similarity(vectors[-1], vectors[:-1])

        # Benzerliği kontrol et
        if cosine_sim.max() > 0.5:
            self.result_label.config(text="Bu mesaj SPAM olarak tespit edildi.", fg="red")
        else:
            self.result_label.config(text="Bu mesaj HAM olarak tespit edildi.", fg="green")
        
        # Yazıyı sil
        self.text_input.delete("1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpamDetectorApp(root)
    root.mainloop()
