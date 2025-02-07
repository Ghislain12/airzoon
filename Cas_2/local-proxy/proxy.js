const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
app.use(cors());

// Liste de vraies publicités
const ads = [
    {
        id: 1,
        image: "https://m.media-amazon.com/images/I/61Iz2yy2CKL._AC_SY450_.jpg",
        link: "https://www.amazon.com/dp/B08N5WRWNW",
        category: "tech",
        title: "Amazon Echo Dot (4th Gen) - Smart speaker with Alexa - Charcoal Fabric",
        description: "Meet Echo Dot 4th Gen, our most popular smart speaker with Alexa. It's our most compact smart speaker that fits perfectly into small spaces and looks great in any room."
    },
    {
        id: 2,
        image: "https://www.nike.com.kw/dw/image/v2/BDVB_PRD/on/demandware.static/-/Sites-akeneo-master-catalog/default/dw96b95243/nk/ac0/4/7/f/4/f/ac047f4f_ce27_4b18_94c4_1d1e77557f09.jpg?sw=700&sh=700&sm=fit&q=100&strip=false",
        link: "https://nike.com/shoes",
        category: "sports",
        title: "Nike Air Max 270",
        description: "The Nike Air Max 270 is a modern take on the iconic Air Max design, featuring a full-length Air unit for unparalleled comfort and a sleek, modern look."
    },
    {
        id: 3,
        image: "https://dtonnqfqmjwtr.cloudfront.net/cache/img/mobile-tablet-167634-767-500-auto.jpg?q=1667554190",
        link: "https://booking.com/hotel",
        category: "travel",
        title: "Booking.com - Hotels, Apartments, Hostels, Motels, Vacation Rentals",
        description: "Find the best hotels, apartments, hostels, motels, vacation rentals, and more on Booking.com."
    }
];

// API qui renvoie les publicités filtrées
app.get("/ads", (req, res) => {
    const userId = req.query.user_id || "default";
    const userPreferences = {
        "123": ["tech", "sports"], // Cet utilisateur veut voir tech et sport
        "456": ["travel"] // Cet utilisateur veut voir uniquement travel
    };

    const allowedCategories = userPreferences[userId] || ["tech", "sports", "travel"];
    const filteredAds = ads.filter(ad => allowedCategories.includes(ad.category));

    res.json({ ads: filteredAds });
});

// Servir la page splash modifiée
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "splash_original.html"));
});

// Démarrer le serveur local
const PORT = 5000;
app.listen(PORT, "0.0.0.0", () => {
  console.log(`Serveur actif sur http://0.0.0.0:${PORT}`);
});
