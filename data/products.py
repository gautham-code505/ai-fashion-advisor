from data.demo_data import get_image_url

# Helper to easily reuse the 30 curated Unsplash images
def img(key):
    return get_image_url(key)

ALL_SKIN = ["Fair", "Wheatish", "Medium", "Olive", "Dark", "Deep"]
ALL_SHAPES = ["Hourglass", "Pear", "Apple", "Rectangle", "Inverted Triangle"]

PRODUCTS = [
    # MALE TOPWEAR
    {
        "id": "p1", "name": "Crisp Cotton Shirt", "gender": ["Men"], "category": "shirts", "outfit_slot": "topwear",
        "occasions": ["Office", "Party", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["White", "Light Blue"], "price": 1499, "rating": 4.5, "image_url": img("shirt"),
        "description": "Classic tailored cotton shirt for formal and semi-formal wear.",
        "reason": "A well-fitted shirt broadens the shoulders and gives a sharp structure.",
        "search_query": "Men's crisp cotton shirt formal"
    },
    {
        "id": "p2", "name": "Casual Graphic T-Shirt", "gender": ["Men", "Unisex"], "category": "t-shirts", "outfit_slot": "topwear",
        "occasions": ["Casual", "College", "Vacation"], "skin_tones": ALL_SKIN, "body_shapes": ["Rectangle", "Inverted Triangle", "Hourglass"],
        "colors": ["Black", "Grey"], "price": 699, "rating": 4.2, "image_url": img("casual_1"),
        "description": "Comfortable cotton t-shirt with a subtle graphic print.",
        "reason": "Perfect for a relaxed vibe while keeping the upper body looking proportionate.",
        "search_query": "Men's casual graphic cotton t-shirt"
    },
    {
        "id": "p3", "name": "Tailored Navy Blazer", "gender": ["Men"], "category": "blazers", "outfit_slot": "topwear",
        "occasions": ["Office", "Party", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ["Rectangle", "Pear", "Apple"],
        "colors": ["Navy Blue"], "price": 3500, "rating": 4.8, "image_url": img("blazer"),
        "description": "Premium wool blend blazer with a slim fit.",
        "reason": "A blazer instantly elevates any outfit and adds structure to the torso.",
        "search_query": "Men's tailored slim fit navy blazer"
    },
    {
        "id": "p4", "name": "Festive Silk Kurta", "gender": ["Men"], "category": "kurtas", "outfit_slot": "topwear",
        "occasions": ["Festival", "Wedding Guest"], "skin_tones": ["Fair", "Wheatish", "Medium", "Olive"], "body_shapes": ALL_SHAPES,
        "colors": ["Maroon", "Gold"], "price": 2200, "rating": 4.6, "image_url": img("festival_1"),
        "description": "Elegant silk blend kurta for traditional occasions.",
        "reason": "Rich colors complement your skin tone beautifully for festive events.",
        "search_query": "Men's traditional silk kurta maroon"
    },
    
    # MALE BOTTOMWEAR
    {
        "id": "p5", "name": "Slim Fit Denim Jeans", "gender": ["Men", "Unisex"], "category": "jeans", "outfit_slot": "bottomwear",
        "occasions": ["Casual", "College", "Party", "Vacation"], "skin_tones": ALL_SKIN, "body_shapes": ["Rectangle", "Inverted Triangle", "Hourglass"],
        "colors": ["Dark Wash Blue"], "price": 1899, "rating": 4.4, "image_url": img("casual_2"),
        "description": "Classic dark wash denim with a comfortable stretch.",
        "reason": "Slim jeans provide a modern silhouette without being restrictive.",
        "search_query": "Men's slim fit dark wash stretch jeans"
    },
    {
        "id": "p6", "name": "Stone Chinos", "gender": ["Men"], "category": "trousers", "outfit_slot": "bottomwear",
        "occasions": ["Office", "College", "Party"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Beige", "Stone"], "price": 1599, "rating": 4.5, "image_url": img("chinos"),
        "description": "Stretch-twill chinos for all-day comfort.",
        "reason": "Chinos offer a versatile smart-casual look that balances out your upper body.",
        "search_query": "Men's slim fit stone chinos"
    },
    {
        "id": "p7", "name": "Formal Tailored Trousers", "gender": ["Men"], "category": "trousers", "outfit_slot": "bottomwear",
        "occasions": ["Office", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Charcoal Grey"], "price": 1799, "rating": 4.7, "image_url": img("office_1"),
        "description": "Sleek formal trousers with a sharp crease.",
        "reason": "Dark trousers elongate the legs and create a professional appearance.",
        "search_query": "Men's formal tailored trousers charcoal"
    },

    # FEMALE TOPWEAR
    {
        "id": "p8", "name": "Chiffon Blouse", "gender": ["Women"], "category": "shirts", "outfit_slot": "topwear",
        "occasions": ["Office", "Party", "College"], "skin_tones": ALL_SKIN, "body_shapes": ["Hourglass", "Pear"],
        "colors": ["Blush Pink", "White"], "price": 1299, "rating": 4.3, "image_url": img("office_2"),
        "description": "Lightweight chiffon blouse with elegant draping.",
        "reason": "The soft draping highlights your natural curves elegantly.",
        "search_query": "Women's elegant chiffon blouse"
    },
    {
        "id": "p9", "name": "Embroidered Kurti", "gender": ["Women"], "category": "kurtas", "outfit_slot": "topwear",
        "occasions": ["Festival", "College", "Casual"], "skin_tones": ALL_SKIN, "body_shapes": ["Apple", "Rectangle", "Pear"],
        "colors": ["Teal", "Mustard"], "price": 1499, "rating": 4.6, "image_url": img("female_1"),
        "description": "Cotton kurti with intricate threadwork.",
        "reason": "The straight cut is incredibly flattering and comfortable for all-day wear.",
        "search_query": "Women's cotton embroidered kurti"
    },
    {
        "id": "p10", "name": "Basic V-Neck Tee", "gender": ["Women", "Unisex"], "category": "t-shirts", "outfit_slot": "topwear",
        "occasions": ["Casual", "College", "Vacation"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Olive Green", "Black"], "price": 599, "rating": 4.1, "image_url": img("casual_1"),
        "description": "Essential v-neck t-shirt in soft modal cotton.",
        "reason": "A v-neck elongates the neck and offers a great casual foundation.",
        "search_query": "Women's basic v-neck modal t-shirt"
    },
    {
        "id": "p11", "name": "Evening Maxi Dress", "gender": ["Women"], "category": "dresses", "outfit_slot": "topwear",
        "occasions": ["Party", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ["Hourglass", "Pear", "Rectangle"],
        "colors": ["Emerald Green"], "price": 2899, "rating": 4.8, "image_url": img("party_1"),
        "description": "Stunning maxi dress with a thigh-high slit.",
        "reason": "The cinched waist and flowing skirt highlight your best features.",
        "search_query": "Women's evening maxi dress emerald"
    },
    {
        "id": "p12", "name": "Classic Silk Saree", "gender": ["Women"], "category": "sarees", "outfit_slot": "topwear",
        "occasions": ["Festival", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Crimson Red", "Gold"], "price": 4500, "rating": 4.9, "image_url": img("wedding_1"),
        "description": "Authentic silk saree with zari border.",
        "reason": "A saree is universally flattering and perfect for festive grandeur.",
        "search_query": "Women's traditional silk saree zari border"
    },

    # FEMALE BOTTOMWEAR
    {
        "id": "p13", "name": "High-Waisted Wide Leg Jeans", "gender": ["Women"], "category": "jeans", "outfit_slot": "bottomwear",
        "occasions": ["Casual", "College", "Party"], "skin_tones": ALL_SKIN, "body_shapes": ["Pear", "Hourglass", "Inverted Triangle"],
        "colors": ["Light Wash Blue"], "price": 1699, "rating": 4.5, "image_url": img("casual_2"),
        "description": "Trendy wide-leg denim that elongates the legs.",
        "reason": "High waists define the waistline while wide legs balance your proportions.",
        "search_query": "Women's high-waisted wide leg jeans"
    },
    {
        "id": "p14", "name": "Tailored Cigarette Pants", "gender": ["Women"], "category": "trousers", "outfit_slot": "bottomwear",
        "occasions": ["Office", "Party"], "skin_tones": ALL_SKIN, "body_shapes": ["Rectangle", "Apple", "Hourglass"],
        "colors": ["Black", "Navy"], "price": 1499, "rating": 4.4, "image_url": img("office_2"),
        "description": "Sleek ankle-length trousers.",
        "reason": "The tapered fit provides a very polished, professional silhouette.",
        "search_query": "Women's tailored cigarette pants office"
    },
    {
        "id": "p15", "name": "Flared Palazzo Pants", "gender": ["Women"], "category": "trousers", "outfit_slot": "bottomwear",
        "occasions": ["Festival", "Casual", "Vacation"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["White", "Beige"], "price": 1199, "rating": 4.2, "image_url": img("festival_2"),
        "description": "Breezy palazzo pants perfect for pairing with kurtis.",
        "reason": "They offer immense comfort and a beautiful fluid movement.",
        "search_query": "Women's flared palazzo pants cotton"
    },

    # FOOTWEAR (MIXED)
    {
        "id": "p16", "name": "Leather Loafers", "gender": ["Men"], "category": "footwear", "outfit_slot": "footwear",
        "occasions": ["Office", "Party", "Casual", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Brown", "Tan"], "price": 1999, "rating": 4.5, "image_url": img("loafers"),
        "description": "Genuine leather loafers with a minimal design.",
        "reason": "Loafers effortlessly bridge the gap between casual and formal.",
        "search_query": "Men's genuine leather loafers brown"
    },
    {
        "id": "p17", "name": "White Minimalist Sneakers", "gender": ["Men", "Women", "Unisex"], "category": "footwear", "outfit_slot": "footwear",
        "occasions": ["Casual", "College", "Vacation"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["White"], "price": 1499, "rating": 4.7, "image_url": img("footwear"),
        "description": "Clean white sneakers that match any casual outfit.",
        "reason": "White sneakers are a modern wardrobe essential that keep the look fresh.",
        "search_query": "Minimalist white casual sneakers"
    },
    {
        "id": "p18", "name": "Nude Block Heels", "gender": ["Women"], "category": "footwear", "outfit_slot": "footwear",
        "occasions": ["Office", "Party", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Nude", "Beige"], "price": 1599, "rating": 4.3, "image_url": img("female_2"),
        "description": "Comfortable block heels for all-day wear.",
        "reason": "Nude heels visually elongate your legs while the block heel provides stability.",
        "search_query": "Women's nude block heels comfortable"
    },
    {
        "id": "p19", "name": "Embellished Mojaris", "gender": ["Men", "Women", "Unisex"], "category": "footwear", "outfit_slot": "footwear",
        "occasions": ["Festival", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Gold", "Tan"], "price": 999, "rating": 4.6, "image_url": img("wedding_2"),
        "description": "Traditional mojaris with subtle embroidery.",
        "reason": "The perfect ethnic footwear to complete your festive ensemble.",
        "search_query": "Traditional embroidered mojaris gold"
    },

    # ACCESSORIES / OPTIONAL
    {
        "id": "p20", "name": "Classic Analog Watch", "gender": ["Men", "Unisex"], "category": "watches", "outfit_slot": "accessory",
        "occasions": ["Office", "College", "Party", "Wedding Guest", "Casual"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Silver", "Black"], "price": 2499, "rating": 4.8, "image_url": img("watch"),
        "description": "Sleek analog dial with a genuine leather strap.",
        "reason": "A minimal watch adds a touch of sophistication to your wrist.",
        "search_query": "Classic analog watch leather strap"
    },
    {
        "id": "p21", "name": "Rose Gold Minimalist Watch", "gender": ["Women"], "category": "watches", "outfit_slot": "accessory",
        "occasions": ["Office", "College", "Party", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Rose Gold"], "price": 2299, "rating": 4.7, "image_url": img("female_1"),
        "description": "Elegant mesh strap watch in rose gold.",
        "reason": "Rose gold warms up the skin tone and looks incredibly chic.",
        "search_query": "Women's rose gold minimalist watch"
    },
    {
        "id": "p22", "name": "Leather Messenger Bag", "gender": ["Men", "Unisex"], "category": "bags", "outfit_slot": "optional",
        "occasions": ["Office", "College"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Brown", "Black"], "price": 1899, "rating": 4.4, "image_url": img("bag"),
        "description": "Spacious leather messenger bag for laptops and essentials.",
        "reason": "Combines practicality with a rugged, professional aesthetic.",
        "search_query": "Leather messenger bag laptop"
    },
    {
        "id": "p23", "name": "Structured Tote Bag", "gender": ["Women"], "category": "bags", "outfit_slot": "optional",
        "occasions": ["Office", "College", "Casual"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Tan"], "price": 1699, "rating": 4.5, "image_url": img("female_2"),
        "description": "Classic tan tote bag with ample space.",
        "reason": "A structured bag pulls the whole look together seamlessly.",
        "search_query": "Women's structured tote bag tan"
    },
    {
        "id": "p24", "name": "Embellished Clutch", "gender": ["Women"], "category": "bags", "outfit_slot": "optional",
        "occasions": ["Party", "Wedding Guest", "Festival"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Gold", "Silver"], "price": 1299, "rating": 4.6, "image_url": img("party_2"),
        "description": "Sparkling evening clutch for special occasions.",
        "reason": "Adds just the right amount of glamour to your festive or party attire.",
        "search_query": "Women's evening embellished clutch gold"
    },
    {
        "id": "p25", "name": "Polarized Sunglasses", "gender": ["Men", "Women", "Unisex"], "category": "glasses", "outfit_slot": "optional",
        "occasions": ["Casual", "Vacation", "College"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Black", "Tortoiseshell"], "price": 999, "rating": 4.2, "image_url": img("glasses"),
        "description": "Classic wayfarer style sunglasses.",
        "reason": "Protects your eyes while adding a cool, mysterious edge to your outfit.",
        "search_query": "Polarized wayfarer sunglasses"
    },
    {
        "id": "p26", "name": "Signature Fresh Perfume", "gender": ["Men", "Women", "Unisex"], "category": "perfumes", "outfit_slot": "optional",
        "occasions": ["Office", "Casual", "College"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Clear"], "price": 1999, "rating": 4.8, "image_url": img("perfume"),
        "description": "A light, aquatic fragrance perfect for daytime.",
        "reason": "A good fragrance leaves a lasting impression wherever you go.",
        "search_query": "Fresh aquatic everyday perfume"
    },
    {
        "id": "p27", "name": "Oud Wood Evening Cologne", "gender": ["Men", "Unisex"], "category": "perfumes", "outfit_slot": "optional",
        "occasions": ["Party", "Wedding Guest", "Festival"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Amber"], "price": 2499, "rating": 4.9, "image_url": img("perfume"),
        "description": "Rich and woody fragrance for the evening.",
        "reason": "A stronger, woody scent matches the intensity of evening events.",
        "search_query": "Oud wood evening cologne men"
    },
    {
        "id": "p28", "name": "Floral Eau De Parfum", "gender": ["Women"], "category": "perfumes", "outfit_slot": "optional",
        "occasions": ["Party", "Wedding Guest", "Festival"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Pink"], "price": 2199, "rating": 4.7, "image_url": img("perfume"),
        "description": "Elegant floral scent with notes of jasmine and rose.",
        "reason": "Floral notes complement elegant evening and festive wear perfectly.",
        "search_query": "Women's floral eau de parfum jasmine"
    },
    {
        "id": "p29", "name": "Silver Chain Necklace", "gender": ["Women", "Men", "Unisex"], "category": "accessories", "outfit_slot": "accessory",
        "occasions": ["Casual", "College", "Party"], "skin_tones": ["Fair", "Olive", "Dark", "Deep"], "body_shapes": ALL_SHAPES,
        "colors": ["Silver"], "price": 499, "rating": 4.1, "image_url": img("casual_1"),
        "description": "Minimalist silver chain.",
        "reason": "Silver pops beautifully against your skin tone and adds subtle detail.",
        "search_query": "Minimalist silver chain necklace"
    },
    {
        "id": "p30", "name": "Gold Pendant Set", "gender": ["Women"], "category": "accessories", "outfit_slot": "accessory",
        "occasions": ["Festival", "Wedding Guest", "Party"], "skin_tones": ["Wheatish", "Medium", "Dark", "Deep"], "body_shapes": ALL_SHAPES,
        "colors": ["Gold"], "price": 899, "rating": 4.6, "image_url": img("wedding_1"),
        "description": "Traditional gold-plated pendant set.",
        "reason": "Gold jewelry brings out the warm undertones in your complexion.",
        "search_query": "Traditional gold plated pendant set"
    },
    
    # FILLING UP TO 40 WITH MORE VARIETY
    {
        "id": "p31", "name": "Polo T-Shirt", "gender": ["Men"], "category": "t-shirts", "outfit_slot": "topwear",
        "occasions": ["College", "Casual", "Vacation"], "skin_tones": ALL_SKIN, "body_shapes": ["Rectangle", "Inverted Triangle"],
        "colors": ["Navy", "White"], "price": 899, "rating": 4.3, "image_url": img("college"),
        "description": "Classic pique polo shirt.",
        "reason": "The collar adds a neat touch to a casual look.",
        "search_query": "Men's classic pique polo shirt"
    },
    {
        "id": "p32", "name": "Linen Blend Shirt", "gender": ["Men", "Unisex"], "category": "shirts", "outfit_slot": "topwear",
        "occasions": ["Vacation", "Casual"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Beige", "Light Blue"], "price": 1399, "rating": 4.5, "image_url": img("casual_1"),
        "description": "Breathable linen shirt for warm days.",
        "reason": "Linen provides a relaxed, effortless texture.",
        "search_query": "Men's breathable linen shirt casual"
    },
    {
        "id": "p33", "name": "Formal Waistcoat", "gender": ["Men"], "category": "blazers", "outfit_slot": "topwear",
        "occasions": ["Wedding Guest", "Party"], "skin_tones": ALL_SKIN, "body_shapes": ["Rectangle", "Inverted Triangle"],
        "colors": ["Grey", "Black"], "price": 1599, "rating": 4.2, "image_url": img("office_1"),
        "description": "Sharp formal waistcoat to layer over shirts.",
        "reason": "Layering creates depth and accentuates a masculine v-shape.",
        "search_query": "Men's formal waistcoat grey"
    },
    {
        "id": "p34", "name": "Denim Jacket", "gender": ["Men", "Women", "Unisex"], "category": "blazers", "outfit_slot": "topwear",
        "occasions": ["College", "Casual", "Vacation"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Blue Wash"], "price": 1999, "rating": 4.6, "image_url": img("college"),
        "description": "Classic trucker denim jacket.",
        "reason": "A denim jacket is the ultimate casual layering piece.",
        "search_query": "Classic blue trucker denim jacket"
    },
    {
        "id": "p35", "name": "A-Line Skirt", "gender": ["Women"], "category": "trousers", "outfit_slot": "bottomwear",
        "occasions": ["Casual", "College", "Party"], "skin_tones": ALL_SKIN, "body_shapes": ["Pear", "Hourglass", "Apple"],
        "colors": ["Black", "Floral"], "price": 1099, "rating": 4.4, "image_url": img("female_1"),
        "description": "Flared A-line skirt.",
        "reason": "The A-line shape beautifully balances your hips and waist.",
        "search_query": "Women's flared A-line skirt"
    },
    {
        "id": "p36", "name": "Silk Dupatta", "gender": ["Women"], "category": "accessories", "outfit_slot": "accessory",
        "occasions": ["Festival", "Wedding Guest"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Red", "Gold"], "price": 899, "rating": 4.7, "image_url": img("wedding_1"),
        "description": "Rich Banarasi silk dupatta.",
        "reason": "Adds a traditional, regal touch to any basic kurti.",
        "search_query": "Women's banarasi silk dupatta red gold"
    },
    {
        "id": "p37", "name": "Chunky Sneakers", "gender": ["Men", "Women", "Unisex"], "category": "footwear", "outfit_slot": "footwear",
        "occasions": ["Casual", "College"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["White", "Multi"], "price": 2199, "rating": 4.5, "image_url": img("college"),
        "description": "Trendy chunky sole sneakers.",
        "reason": "Provides all-day comfort while keeping your street style on point.",
        "search_query": "Trendy chunky sole sneakers"
    },
    {
        "id": "p38", "name": "Chelsea Boots", "gender": ["Men", "Unisex"], "category": "footwear", "outfit_slot": "footwear",
        "occasions": ["Party", "Office", "Casual"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Black", "Suede Brown"], "price": 2599, "rating": 4.8, "image_url": img("party_1"),
        "description": "Sleek slip-on Chelsea boots.",
        "reason": "Boots add a sharp, elevated edge to both jeans and trousers.",
        "search_query": "Men's slip-on chelsea boots black"
    },
    {
        "id": "p39", "name": "Printed Sundress", "gender": ["Women"], "category": "dresses", "outfit_slot": "topwear",
        "occasions": ["Vacation", "Casual", "College"], "skin_tones": ALL_SKIN, "body_shapes": ["Apple", "Rectangle", "Hourglass"],
        "colors": ["Yellow", "White"], "price": 1499, "rating": 4.3, "image_url": img("casual_2"),
        "description": "Breezy floral sundress.",
        "reason": "The bright print and relaxed fit are perfect for a sunny day out.",
        "search_query": "Women's breezy floral sundress yellow"
    },
    {
        "id": "p40", "name": "Statement Belt", "gender": ["Men", "Women", "Unisex"], "category": "accessories", "outfit_slot": "accessory",
        "occasions": ["Office", "Party", "Casual"], "skin_tones": ALL_SKIN, "body_shapes": ALL_SHAPES,
        "colors": ["Black", "Brown"], "price": 699, "rating": 4.5, "image_url": img("office_1"),
        "description": "Reversible leather belt with a minimal buckle.",
        "reason": "A good belt cinches the waist and ties the upper and lower halves together.",
        "search_query": "Reversible leather belt minimal buckle"
    }
]
