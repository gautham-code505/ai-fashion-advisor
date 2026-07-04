# data/demo_data.py

# A reliable set of direct Unsplash URLs mapped to categories
BASE_URL = "https://images.unsplash.com/photo-{id}?w=800&q=80"

IDS = {
    "office_1": "1483985988355-763728e1935b",
    "office_2": "1509319111365-f506e7884144",
    "college": "1515886657613-9f3515b0c78f",
    "casual_1": "1529139574466-a303027c1d8b",
    "casual_2": "1541099649105-f69ad21f3246",
    "party_1": "1539109136881-3be0616acf4b",
    "party_2": "1516483638261-f4efa33a0b16",
    "festival_1": "1514525253161-7a46d19cd819",
    "festival_2": "1506152983158-74aa029ed48b",
    "blazer": "1591047139829-d91aecb6caea",
    "shirt": "1620799140408-edc6dcb6d633",
    "chinos": "1624378439575-d8705ad7ae80",
    "loafers": "1614252369475-531eba835eb1",
    "watch": "1523275335684-37898b6baf30",
    "bag": "1584916201218-f4242ceb4809",
    "glasses": "1511499767150-a48a237f0083",
    "perfume": "1594035910387-fea47794261f",
    "female_1": "1434389678396-513b45155883",
    "female_2": "1539109136881-3be0616acf4b",
    "male_1": "1492288991661-058aa541ff43",
    "male_2": "1507003211169-0a1dd7228f2d",
    "wedding_1": "1496747611176-843222e1e57c",
    "wedding_2": "1519741497674-611481863552",
    "footwear": "1523381294911-8d3ce31c9e63"
}

def get_image_url(key):
    return BASE_URL.format(id=IDS.get(key, "1515886657613-9f3515b0c78f"))

TRENDING_COLLECTIONS = [
    {
        "title": "Office Wear",
        "subtitle": "Elevate your daily hustle",
        "image_url": get_image_url("office_1"),
        "span_class": "md:col-span-2 md:row-span-2",
        "height_class": "h-48 md:h-auto",
        "title_class": "text-headline-md font-headline-md text-on-primary",
        "subtitle_class": "text-body-md font-body-md text-on-primary/80 mt-1"
    },
    {
        "title": "College Essentials",
        "image_url": get_image_url("college"),
        "span_class": "md:col-span-1 md:row-span-1",
        "height_class": "h-40 md:h-auto",
        "title_class": "text-label-md font-label-md text-on-primary",
        "subtitle_class": ""
    },
    {
        "title": "Casual Fits",
        "image_url": get_image_url("casual_1"),
        "span_class": "md:col-span-1 md:row-span-1",
        "height_class": "h-40 md:h-auto",
        "title_class": "text-label-md font-label-md text-on-primary",
        "subtitle_class": ""
    },
    {
        "title": "Party Looks",
        "image_url": get_image_url("party_1"),
        "span_class": "md:col-span-1 md:row-span-1",
        "height_class": "h-40 md:h-auto",
        "title_class": "text-label-md font-label-md text-on-primary",
        "subtitle_class": ""
    },
    {
        "title": "Festival Styles",
        "image_url": get_image_url("festival_1"),
        "span_class": "md:col-span-1 md:row-span-1",
        "height_class": "h-48 md:h-auto",
        "title_class": "text-label-md font-label-md text-on-primary",
        "subtitle_class": ""
    }
]

CURATED_PRODUCTS = [
    {
        "title": "Tailored Navy Blazer",
        "price": "$145",
        "description": "Premium wool blend, slim fit.",
        "image_url": get_image_url("blazer")
    },
    {
        "title": "Crisp Cotton Shirt",
        "price": "$65",
        "description": "100% organic cotton, wrinkle-resistant.",
        "image_url": get_image_url("shirt")
    },
    {
        "title": "Stone Chinos",
        "price": "$85",
        "description": "Stretch-twill for all-day comfort.",
        "image_url": get_image_url("chinos")
    },
    {
        "title": "Leather Loafers",
        "price": "$50",
        "description": "Genuine leather, minimal design.",
        "image_url": get_image_url("loafers")
    },
    {
        "title": "Minimalist Watch",
        "price": "$120",
        "description": "Sleek analog dial, leather strap.",
        "image_url": get_image_url("watch")
    },
    {
        "title": "Classic Sunglasses",
        "price": "$90",
        "description": "Polarized lenses, timeless frame.",
        "image_url": get_image_url("glasses")
    }
]
