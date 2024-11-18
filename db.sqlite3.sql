BEGIN TRANSACTION;
DROP TABLE IF EXISTS "django_migrations";
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "auth_group_permissions";
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_user_groups";
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_user_user_permissions";
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "django_admin_log";
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "django_content_type";
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "auth_permission";
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "auth_group";
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "auth_user";
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "store_category";
CREATE TABLE IF NOT EXISTS "store_category" (
	"id"	integer NOT NULL,
	"name"	varchar(250) NOT NULL,
	"slug"	varchar(250) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "store_product";
CREATE TABLE IF NOT EXISTS "store_product" (
	"id"	integer NOT NULL,
	"title"	varchar(250) NOT NULL,
	"brand"	varchar(250) NOT NULL,
	"description"	text NOT NULL,
	"slug"	varchar(255) NOT NULL,
	"price"	decimal NOT NULL,
	"image"	varchar(100) NOT NULL,
	"category_id"	bigint,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("category_id") REFERENCES "store_category"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "payment_order";
CREATE TABLE IF NOT EXISTS "payment_order" (
	"id"	integer NOT NULL,
	"full_name"	varchar(300) NOT NULL,
	"email"	varchar(255) NOT NULL,
	"shipping_address"	text NOT NULL,
	"amount_paid"	decimal NOT NULL,
	"date_ordered"	datetime NOT NULL,
	"user_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "payment_orderitem";
CREATE TABLE IF NOT EXISTS "payment_orderitem" (
	"id"	integer NOT NULL,
	"quantity"	bigint unsigned NOT NULL CHECK("quantity" >= 0),
	"price"	decimal NOT NULL,
	"order_id"	bigint,
	"product_id"	bigint,
	"user_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("order_id") REFERENCES "payment_order"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("product_id") REFERENCES "store_product"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "payment_shippingaddress";
CREATE TABLE IF NOT EXISTS "payment_shippingaddress" (
	"id"	integer NOT NULL,
	"full_name"	varchar(300) NOT NULL,
	"email"	varchar(255) NOT NULL,
	"address1"	varchar(300) NOT NULL,
	"address2"	varchar(300) NOT NULL,
	"city"	varchar(255) NOT NULL,
	"state"	varchar(255),
	"zipcode"	varchar(255),
	"user_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
DROP TABLE IF EXISTS "django_session";
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2024-11-18 07:31:38.562697'),
 (2,'auth','0001_initial','2024-11-18 07:31:38.576322'),
 (3,'admin','0001_initial','2024-11-18 07:31:38.585838'),
 (4,'admin','0002_logentry_remove_auto_add','2024-11-18 07:31:38.594061'),
 (5,'admin','0003_logentry_add_action_flag_choices','2024-11-18 07:31:38.599590'),
 (6,'contenttypes','0002_remove_content_type_name','2024-11-18 07:31:38.611260'),
 (7,'auth','0002_alter_permission_name_max_length','2024-11-18 07:31:38.618763'),
 (8,'auth','0003_alter_user_email_max_length','2024-11-18 07:31:38.626845'),
 (9,'auth','0004_alter_user_username_opts','2024-11-18 07:31:38.632920'),
 (10,'auth','0005_alter_user_last_login_null','2024-11-18 07:31:38.641418'),
 (11,'auth','0006_require_contenttypes_0002','2024-11-18 07:31:38.645418'),
 (12,'auth','0007_alter_validators_add_error_messages','2024-11-18 07:31:38.650442'),
 (13,'auth','0008_alter_user_username_max_length','2024-11-18 07:31:38.658442'),
 (14,'auth','0009_alter_user_last_name_max_length','2024-11-18 07:31:38.665909'),
 (15,'auth','0010_alter_group_name_max_length','2024-11-18 07:31:38.673675'),
 (16,'auth','0011_update_proxy_permissions','2024-11-18 07:31:38.678694'),
 (17,'auth','0012_alter_user_first_name_max_length','2024-11-18 07:31:38.686227'),
 (18,'store','0001_initial','2024-11-18 07:31:38.692744'),
 (19,'payment','0001_initial','2024-11-18 07:31:38.725783'),
 (20,'sessions','0001_initial','2024-11-18 07:31:38.732195');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'store','category'),
 (8,'store','product'),
 (9,'payment','order'),
 (10,'payment','orderitem'),
 (11,'payment','shippingaddress');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_category','Can add category'),
 (26,7,'change_category','Can change category'),
 (27,7,'delete_category','Can delete category'),
 (28,7,'view_category','Can view category'),
 (29,8,'add_product','Can add product'),
 (30,8,'change_product','Can change product'),
 (31,8,'delete_product','Can delete product'),
 (32,8,'view_product','Can view product'),
 (33,9,'add_order','Can add order'),
 (34,9,'change_order','Can change order'),
 (35,9,'delete_order','Can delete order'),
 (36,9,'view_order','Can view order'),
 (37,10,'add_orderitem','Can add order item'),
 (38,10,'change_orderitem','Can change order item'),
 (39,10,'delete_orderitem','Can delete order item'),
 (40,10,'view_orderitem','Can view order item'),
 (41,11,'add_shippingaddress','Can add shipping address'),
 (42,11,'change_shippingaddress','Can change shipping address'),
 (43,11,'delete_shippingaddress','Can delete shipping address'),
 (44,11,'view_shippingaddress','Can view shipping address');
INSERT INTO "store_category" ("id","name","slug") VALUES (1,'shoes','shoes'),
 (2,'shirts','shirts'),
 (3,'Hoodies & Sweatshirt','hoodies-sweatshirt'),
 (4,'Dresses','dresses'),
 (5,'Tops','tops'),
 (6,'Pants','pants'),
 (7,'Coats & Jackets','coats-jackets');
INSERT INTO "store_product" ("id","title","brand","description","slug","price","image","category_id") VALUES (14,'Dark green shirt','un-branded','Stylish.','dark-green-shirt',9.99,'images/Dark_green_shirt.jpg',2),
 (15,'Mineral blue shirt','un-branded','Trendy.','mineral-blue-shirt',9.99,'images/Mineral_blue_shirt.jpg',2),
 (16,'Marvin''s black shoes','Marvin','The latest in shoe fashion.','marvins-black-shoes',19.99,'images/Marvins_black_shoes.jpg',1),
 (17,'Marvin''s brown shoes','un-branded','The latest in shoe fashion.','marvins-brown-shoes',19.99,'images/Marvins_brown_shoes.jpg',1),
 (19,'Women''s Tasman Slippers','un-branded','Product Features
Round-toe slip-on slippers
UGGpure™ wool helps wick away moisture; braided trim
Lightweight and flexible molded EVA with patented tread design for both indoor and outdoor use
Pieced, dyed sheepskin
Fur origin: United States, UK, Spain, Ireland or Australia
17mm sheepskin lining
This product was made in a factory that supports women in our supply chain with the help of HERproject, a collaborative initiative that creates partnerships with brands like ours to empower and educate women in the workplace
Suede upper; sheepskin lining; Treadlite by UGG™ sole
Imported','womens-tasman-slippers',99,'images/WeChatc334e9ee7c2c83dfc75faeee6526389a.jpg',1),
 (20,'Women''s Original Chelsea Boots','un-branded','FSC-certified natural rubber upper with polyester lining
Waterproof handcrafted construction
Vulcanized design for maximum protection
Slip-on design with elastic gusset and nylon pull tab for easy on-off accessibility
Hunter brand detailing for signature style
Style no. WCHELSEA
Synthetic upper; rubber sole
Wipe Clean
Imported','womens-original-chelsea-boots',59,'images/WeChat5e928d2172638e403f6be9c699d458e9.jpg',1),
 (21,'Women''s Boston Soft Footbed Suede Leather Clogs from Finish Line','un-branded','Open heel clog with closed toes
Single strap with buckle detail for customization
Suede upper and footbed lining
Anatomically-shaped soft footbed
Ethylene vinyl acetate (EVA) outsole for grippy traction
Style number- 660473
European Sizing
Suede Upper, Ethylene vinyl acetate (EVA) Sole
Wipe Clean
Imported','womens-boston-soft-footbed-suede-leather-clogs-from-finish-line',89,'images/WeChatb3aa241c4e11e2a19cbdbc2504251436.jpg',1),
 (22,'Women''s 327 Casual Sneakers','un-branded','Heritage running silhouette inspired by 70s sneakers
Supple suede and nylon upper
Lace-up construction offers a snug fit
Well-cushioned midsole delivers unmatched comfort
Rubber traction outsole with pods for enhanced durability
Style number- WS327RA
Women''s athletic footwear from Finish Line
Suede and Synthetic Upper, Rubber Sole
Spot Clean
Imported','womens-327-casual-sneakers',79,'images/WeChat11e18ef0db3fcf4e12a0c0d8aa4e3b84.jpg',1),
 (23,'Women''s Colorblocked Quarter-Zip Sweatshirt','un-branded','Long sleeves
Imported
Mock neck with quarter zipper
Colorblocked body and sleeves; signature logo at chest','womens-colorblocked-quarter-zip-sweatshirt',19.99,'images/WeChat0c528e293ae5237f84b09881947f227c.jpg',3),
 (24,'Women''s Classic Hoodie','un-branded','Contrast whip-stitch trim
Attached hood with crossover neckline; pulls on
Imported
On-seam pockets
Long raglan sleeves','womens-classic-hoodie',29,'images/WeChat35ea1934dbe92934944384ab3030fa08.jpg',3),
 (25,'Women''s Camden Henley Balloon-Sleeve Top','un-branded','Drop shoulder long balloon sleeves; fitted slit cuffs
ABOUT THE BRAND: If you love the laid-back charm of boho-chic apparel, you''ll find a beautiful selection from Free People at Macy''s that suits your style. From ultra-feminine dresses to cute tops, browse the collection of casual, hip designs.
Made in USA
Seaming details; slit high-low hem
Collared Henley neckline; pulls on with partial snap closures
Size & Fit
Approx. 25-3/4" long
Materials & Care
Machine wash
51% cotton, 49% polyester','womens-camden-henley-balloon-sleeve-top',20,'images/WeChat9fef41aa3dc8272ddc30f2694857857b.jpg',3),
 (26,'Women''s Sherpa Mock-Neck Zippered Sweater','un-branded','Long sleeves
Stand collar; front zip closure
Colorblock sherpa design
Zippered hip pockets
Imported
Size & Fit
Approx. 25-1/4" long
Materials & Care
Machine wash
Nylon chest patch with logo detail
100% polyester; trim: 100% nylon','womens-sherpa-mock-neck-zippered-sweater',39,'images/WeChat905d8017bc77926c11cb7d86ac3cacd2.jpg',3),
 (27,'Women''s Rib Knit Turtleneck Sweater Dress','un-branded','Imported
Pulls on
Unlined
Materials & Care
100% Merino wool
Machine wash
Shipping & Returns
This item qualifies for Free Shipping with minimum purchase! exclusions & details
Enjoy a longer window to return most of your holiday purchases. See our Extended Holiday Return Policy to see if this item qualifies.
California and Minnesota customers call 1-800-289-6229 for Free Shipping information.
Returns are accepted at any Macy''s store within 30 days from purchase date. Last Act items are final sale and sold "as is." No returns, exchanges, or price adjustments allowed.
For complete details, see our Shipping and Returns policies.','womens-rib-knit-turtleneck-sweater-dress',99,'images/WeChat24884248ab46cd605add1b4411c26434.jpg',4),
 (28,'Women''s Clara Dress','un-branded','Product Features
Designed in NYC | Handcrafted in Europe
Sleeveless
Scoopneck tank dress, with an a-line flared skirt
Imported
60% VIS 30% PA 10% LY
Fitted bodice with mid stretch, full skirt
Size & Fit
Approx. 53" long
Materials & Care
Machine washable','womens-clara-dress',59,'images/WeChatd5f7dc178b6dec2e0739a1b1bbc41c90.jpg',4),
 (29,'Women''s Plaid Ruffle-Trim Georgette Tiered Dress','un-branded','Imported
Ruffle-trimmed tiered skirt
Band collar
Curved front lap yoke
Elasticized waist creates a blouson effect
Fully lined except for the sleeves
Ruffle-trimmed buttoned half-placket
Shirring into the cuffs and the back of the neck
Ruffle-trimmed raglan seams
Threaded belt loops; comes with a removable self-belt
Ruffle-trimmed blouson sleeves with elasticized cuffs','womens-plaid-ruffle-trim-georgette-tiered-dress',89,'images/WeChata9427b07aa26882aea49c4caa568d176.jpg',4),
 (30,'Women''s Scuba One-Shoulder Bow Skater Midi Dress','un-branded','Bow Detail
Imported
IMPORTANT NOTE: We do not accept worn, washed, damaged, or altered items. Products missing the tag are ineligible for a refund.
Scuba fabric: Thick foamy, stretchy, and structured, known for its resilience and support','womens-scuba-one-shoulder-bow-skater-midi-dress',99,'images/WeChat8852a9b0640d2f914e5e712785ed2cdd.jpg',4),
 (31,'Women''s Double-Breasted Overcoat','un-branded','Long sleeves
Notched collar; front double-breasted button closures
Imported
Two welt pockets at front
Lined
Created for Macy''s','womens-double-breasted-overcoat',69,'images/WeChat2015894b221d16778c3c1d051420a36a.jpg',7),
 (32,'Bullion Jacquard Blazer','un-branded','Two-button silhouette
Gold-tone crest-embossed buttons
Two front waist flapped pockets
Left chest patch pocket
Long sleeves with four-button cuffs
Imported
Bullion LRL patch embroidered at the left chest
Notch lapels
Connect with a stylist & get free expert advice online or in stores for your wardrobe, home & more. Book Now','bullion-jacquard-blazer',69,'images/WeChata60111d1f44bb954f60f72f98bf7eb2b.jpg',7),
 (33,'Women''s Quilted Velboa-Lined Coat','un-branded','Imported
Long sleeves
Two front waist snapped patch pockets; "LRL"-engraved metal snaps','womens-quilted-velboa-lined-coat',88,'images/WeChat5ecc3d918c7b9881232356eccaa9b59d.jpg',7),
 (34,'Women''s Shine Hooded Anorak Puffer Coat','un-branded','Imported
Black-tone hardware; adjustable bungee at waist
Lined
Zippered hip pockets
Stand collar with fixed adjustable bungee hood; front zip closure
Water resistant','womens-shine-hooded-anorak-puffer-coat',77,'images/WeChatc20e3408581c7c3464818e28b98392b8.jpg',7),
 (35,'Donna Karan Women''s A-Line Button Down Poplin Tunic','un-branded','Unlined
Imported
Covered button front closure
On-seam pockets at sides','donna-karan-womens-a-line-button-down-poplin-tunic',12,'images/WeChat2a21773dc29d63068099e2e1058dcdb8.jpg',2),
 (36,'Donna Karan Women''s Button Front Collared Shirt','un-branded','Curved high-low hem; buttoned cuffs
Imported
Point collar; internal front button closures','donna-karan-womens-button-front-collared-shirt',23,'images/WeChat850bf228d19f3a8a197a9c9506751a3c.jpg',2),
 (37,'Women''s Collared Tie-Waist Shirt','un-branded','Imported
Front button closures','womens-collared-tie-waist-shirt',34,'images/WeChat1957a25d5e0539e4c2e13e389b667b82.jpg',2),
 (38,'Donna Karan Women''s Sleeveless Faux-Wrap Blouse','un-branded','Size & Fit
Approx. 23-3/4" long
Materials & Care
95% polyester, 5% spandex
Hand wash','donna-karan-womens-sleeveless-faux-wrap-blouse',45,'images/WeChat87501b911d92aa460839b1d8dda62a87.jpg',2),
 (39,'Women''s Rhinestone Crewneck Top','un-branded','Long sleeves
Crewneck with rhinestones; back button closure
Imported','womens-rhinestone-crewneck-top',10,'images/WeChat6c782d37402905a498cf84fc0e6fa166.jpg',5),
 (40,'Women''s Bow Neck Cotton T-Shirt','un-branded','Short sleeves
Imported
Bow accent at neck
Crewneck; pulls on','womens-bow-neck-cotton-t-shirt',9,'images/WeChatca1fe3597c05d7766466ff137991e501.jpg',5),
 (41,'Women''s Cotton Contrast Puff-Sleeve Polo','un-branded','Imported
Short sleeves; puffed shoulders
Polo collar; button-closure quarter placket
Contrast trim','womens-cotton-contrast-puff-sleeve-polo',20,'images/WeChat5d2af2eb509d4c2395dce9430c482362.jpg',5),
 (42,'Women''s Embellished Pocket Crewneck T-Shirt','un-branded','Short sleeves
Embellished patch pocket at chest
Imported
Crewneck; pulls on','womens-embellished-pocket-crewneck-t-shirt',22,'images/WeChat1b3f05879fb03fa85bfa9d3fa7bab8a5.jpg',5),
 (43,'Women''s Rib-Knit Pants','un-branded','Front rise: approx. 10-3/4; back rise: approx. 16-1/4"
Approx. inseam: 30"','womens-rib-knit-pants',43,'images/WeChat507a59510eca8a4e1d830eb9f8f68dbf.jpg',6),
 (44,'Donna Karan Women''s Metallic Wide-Leg Pants','un-branded','Approx. inseam: 31-1/2"
Front rise: approx. 12"; back rise: approx. 16-1/4"; wide leg','donna-karan-womens-metallic-wide-leg-pants',79,'images/WeChat3fa5d3954e130f43d233c66cdd657a3c.jpg',6),
 (45,'Women''s 100% Linen Drawstring Pants','un-branded','Slit pockets at hips; decorative welt pockets at back
Pull-on styling; adjustable drawstring waistband
Imported
Created for Macy''s
Connect with a stylist & get free expert advice online or in stores for your wardrobe, home & more. Book Now','womens-100-linen-drawstring-pants',49,'images/WeChat864321663ebc5d9cabf30f0c54e49a18.jpg',6),
 (46,'Women''s Faux-Leather Straight Pants, Created for Macy''s','un-branded','This product was made in a factory where RISE programs advance women''s empowerment and gender equality
High rise: approx. XX"; leg opening: approx. XX"
Zipper and button closure at front; belt loops','womens-faux-leather-straight-pants-created-for-macys',89,'images/WeChat9e8c89d9976db9adf71e10ee04396f0d.jpg',6),
 (47,'Women''s Faux-Fur-Lined Hooded Puffer Coat','Calvin Klein','Start something stylish in this hooded puffer coat from Calvin Klein designed with chic faux fur that peeks out the collar and hood.','womens-faux-fur-lined-hooded-puffer-coat',89.99,'images/27680731_xUNoHgC.jpg',7),
 (48,'Men''s Quilted Puffer Jacket','Tommy Hilfiger','Ribbed-knit storm cuffs add warmth to this wind and water-resistant puffer jacket from Tommy Hilfiger, designed with an attached hood lined with cozy micro-fleece for a soft touch.','mens-quilted-puffer-jacket',79.99,'images/22937634.jpg',7),
 (49,'Womens Asymmetrical Belted Wrap Coat','Calvin Klein','Give your look a gorgeous finish with this wrap coat from Calvin Klein, designed with a waist-defining belt and shawl collar.','womens-asymmetrical-belted-wrap-coat',99,'images/22115338.jpg',7),
 (50,'Men''s Quilted Hooded Puffer Jacket','Michael Kors','Quilted puffer styling and secure storm cuffs make this hooded jacket from Michael Kors the perfect choice for keeping things cozy and warm in colder weather.','mens-quilted-hooded-puffer-jacket',79.9,'images/29603963.jpg',7),
 (51,'Men''s Mixed-Media Puffer Jacket','Tommy Hilfiger','A modern take on the classic puffer jacket, this mixed-media style from Tommy Hilfiger features a fun design and performance details that''ll keep you warm in the storm.','mens-mixed-media-puffer-jacket',87.6,'images/28231314.jpg',7),
 (52,'GUESS Men''s Hooded Puffer Coat','GUESS','Warm and lightweight, this essential bomber jacket from GUESS offers all-weather protection and features a removable hood for added versatility.','guess-mens-hooded-puffer-coat',98.9,'images/25432114.jpg',7),
 (53,'Men''s Logo-Patch Mixed-Media Varsity Jacket','Champion','Earn your varsity letter in style with this Champion jacket. The updated bomber features bold logo patches and sleek faux-leather sleeves.','mens-logo-patch-mixed-media-varsity-jacket',96,'images/28628731.jpg',7),
 (54,'Women''s Houndstooth Pants','Calvin Klein','Update your work wardrobe with these chic houndstooth pants from Calvin Klein.','womens-houndstooth-pants',45.9,'images/29695332.jpg',6),
 (55,'Men''s Modern-Fit TH Flex Stretch Solid Performance Pants','Tommy Hilfiger','Maximize your professional style and comfort while keeping your look crisp with the modern tailoring and wrinkle-resistant TH Flex stretch design of these dress pants from Tommy Hilfiger.','mens-modern-fit-th-flex-stretch-solid-performance-pants',48.9,'images/9248304.jpg',6),
 (56,'Men''s Slim-Fit Modern Stretch Chino Pants','Calvin Klein','Perfect for traveling, long days at work and anything in-between, these pants from Calvin Klein help keep your look comfortable and crisp with their streamlined slim fit and wrinkle-resistant stretch fabric.','mens-slim-fit-modern-stretch-chino-pants',43.99,'images/16457279.jpg',6),
 (57,'Men''s Modern-Fit Stretch Pants','Perry Ellis Portfolio','Topped with a crisp pleat, these stretch pants from Perry Ellis Portfolio are cut for a modern fit that helps build you a modern look.','mens-modern-fit-stretch-pants',19.93,'images/27609322.jpg',6),
 (58,'Men''s Modern-Fit Linen Dress Pants','Nautica','Classic deep-tone blue combines with breathable linen design to give you these airy, elegant modern-fit dress pants from Nautica.','mens-modern-fit-linen-dress-pants',39.99,'images/25989600.jpg',6),
 (59,'Men''s Core Jogger Pant','True Religion','Designed from a comfy cotton blend, these True Religion jogger sweatpants feature an easy elasticized drawstring waistband and a tapered ankle hem.','mens-core-jogger-pant',54.5,'images/29886688.jpg',6),
 (60,'Men''s Dean WX UL Faux-Leather Rugged Casual Hiker Chukka Boots','Levi''s','A stylish blend of a classic work boot and a chukka, this Dean WX UL faux-leather pair from Levi''s® pair perfectly with your favorite jeans.','mens-dean-wx-ul-faux-leather-rugged-casual-hiker-chukka-boots',29.99,'images/20383739.jpg',1),
 (61,'Men''s Maxxin Mid Height Chelsea Boot','Madden Men','Whether you''re heading to work or weekend fun, the sleek and stylish Maxxin Chelsea Boot by Madden Men will provide you with style and comfort. Pull-on style featuring elasticized insets and for easy on and off wear, these comfortable boots provide you with versatility and will become a favorite.','mens-maxxin-mid-height-chelsea-boot',29.99,'images/22638377.jpg',1),
 (62,'Men''s Westin Lace-Up Boots, Created for Macy''s','Club Room','Bring a modern feel to your business-ready look with these dress boots from Club Room, featuring sleek faux-leather uppers and padded collars for all-day comfort.','mens-westin-lace-up-boots-created-for-macys',19.99,'images/22240381.jpg',1),
 (63,'Women''s Charmanee Tall Boots, Created for Macy''s','Style & Co','An asymmetrical topline and clean lines complete a versatile addition to any wardrobe in the fresh Charmanee riding boots from Style & Co.','womens-charmanee-tall-boots-created-for-macys',19.99,'images/25334721.jpg',1),
 (64,'Women''s Collared Button-Down Shirt, Created for Macy’s','On 34th','Polished, versatile, and fitted just right, The Relaxed-To-Refined Button Down is a classic staple that gives you the room to dress it up or down based on your mood, schedule, or occasion. ABOUT THE BRAND: Our new brand was designed for and with women like you. Made for your body, your style, and your truth. As your wardrobe''s best friend, these mix-and-match pieces work with everything in your closet.','womens-collared-button-down-shirt-created-for-macys',22.25,'images/24343722.jpg',2),
 (65,'Men''s Classic-Fit Performance Twill Shirt','Polo Ralph Lauren','Polo Ralph Lauren''s shirt is crafted from a stretchy twill fabric that is made with COOLMAX® fibers to help keep you cool, dry, and comfortable.','mens-classic-fit-performance-twill-shirt',82.8,'images/23085683.jpg',2),
 (66,'Men''s Long Sleeve Brushed Jersey Henley T-shirt','Weatherproof Vintage','Take the effort out of deciding what to wear with this simple heathered Henley from Weatherproof Vintage that goes with just about everything.','mens-long-sleeve-brushed-jersey-henley-t-shirt',19.99,'images/10057356.jpg',2),
 (67,'Men''s Lived-in Long Sleeve Workwear Shirt','Lucky Brand','When the temps take a dip, reach for this lived-in long sleeve workwear shirt by Lucky Brand. Made from soft cotton-rayon fabric for a lived-in look and feel, this button down shirt features classic workwear detailing like a timeless spread collar and double chest pockets. Style with jeans or chinos to complete the laid-back look.','mens-lived-in-long-sleeve-workwear-shirt',29.81,'images/29706989.jpg',2),
 (68,'Women''s Club Fleece Collection','Nike','Whether you''re heading to the gym or just out to run some errands, let Nike keep you warm and comfortable in its Club Fleece Collection.','womens-club-fleece-collection',24.5,'images/25360447.jpg',3),
 (69,'Men''s Fleece Pullover Hoodie','Nike','For a toasty, top-to-bottom look, suit up in Nike''s matching hoodie and joggers and complete your ensemble with a classic club T-shirt and signature all-white sneakers.','mens-fleece-pullover-hoodie',48.75,'images/25774621.jpg',3),
 (70,'Men''s Sportswear Club Fleece Pullover Hoodie','Nike','A timeless staple, this Nike Sportswear hoodie is in soft, brushed-back fleece for classic comfort.','mens-sportswear-club-fleece-pullover-hoodie',29.24,'images/27334953.jpg',3),
 (71,'Men''s Long Sleeve Sportswear Club T-Shirt','Nike','Classic comfort in a sleek look. This long-sleeve Nike logo T-shirt sets you up with a soft cotton jersey feel and Nike''s signature logo embroidered on the chest.','mens-long-sleeve-sportswear-club-t-shirt',24.5,'images/13754313.jpg',3),
 (72,'Men''s Academy Dri-FIT Soccer Top','Nike','Inspired by the look of soccer training tops from the 1990s, this sweat-wicking logo shell helps keep you dry and cool on the field and beyond. Made with a relaxed, lightweight fit, it can be worn on warm and cool days alike.','mens-academy-dri-fit-soccer-top',33.74,'images/26703029.jpg',3),
 (73,'Men''s Sportswear Club Fleece Embroidered Logo Sweatshirt','Nike','Take on the day (or just cozy up on the couch to catch up on your favorite shows) in comfort with this easy-to-style sweatshirt from Nike, featuring a comfortable fit in soft brushed fleece.','mens-sportswear-club-fleece-embroidered-logo-sweatshirt',29.99,'images/25465259.jpg',3),
 (74,'Women''s Long-Sleeve Wrap Dress','Calvin Klein','Calvin Klein updates this long sleeve wrap-inspired design with hardware detailing at the front and a luxurious finish.','womens-long-sleeve-wrap-dress',96.99,'images/29838846.jpg',4),
 (75,'Women''s Sequined Wrap Dress, Created for Macy''s','I.N.C. International Concepts','I.N.C. International Concepts® takes your look in a dazzling direction with this dreamy wrap dress designed with sequins that sparkle with every step.','womens-sequined-wrap-dress-created-for-macys',49.75,'images/29123215.jpg',4),
 (76,'Petites Velvet Wrap Mini Dress, Created for Macy''s','I.N.C. International Concepts','Get ready for all the holiday parties ahead with this luxe velvet wrap dress by I.N.C. International Concepts®.','petites-velvet-wrap-mini-dress-created-for-macys',44.75,'images/29186242_Wh8coi3.jpg',4),
 (77,'Family Matching Plus Size Velvet Long-Sleeve Dress, Created for Macy''s','I.N.C. International Concepts','Plush, posh, and perfect for parties, you can match with your mini-me in this all-velvet dress from I.N.C. International Concepts®, available in little girls'' sizes, too!','family-matching-plus-size-velvet-long-sleeve-dress-created-for-macys',44.75,'images/24272990.jpg',4),
 (78,'Women''s Quarter-Zip Sweater Mini Dress, Created for Macy''s','On 34th','You''ve got options galore with our half-zip sweater dress. Wear it zipped down like a sailor-style collar, or layer it over leggings like a tunic when the weather gets cold. ABOUT THE BRAND: Our brand was designed for, and with women like you. Made for your body, your style, and your truth. As your wardrobe''s best friend, these mix-and-match pieces work with everything in your closet.','womens-quarter-zip-sweater-mini-dress-created-for-macys',35.77,'images/29141609.jpg',4),
 (79,'Women''s Shine Metallic Tie-Waist Dress','Tommy Hilfiger','Chic, shimmery fabric energizes this Tommy Hilfiger dress, giving the timeless silhouette fresh appeal.','womens-shine-metallic-tie-waist-dress',49.75,'images/28783412.jpg',4),
 (80,'Women''s Textured Pintuck Ruffle Sleeve Top, Regular & Petite, Created for Macy''s','Style & Co','Style & Co® textured this top with Swiss dots and front pleats for a more interesting finish. Use it to dress up a pair of jeans for a weekend date.','womens-textured-pintuck-ruffle-sleeve-top-regular-petite-created-for-macys',34.75,'images/29533548.jpg',5),
 (81,'Women''s Printed Pintuck Ruffle Sleeve Top, Regular & Petite, Created for Macy''s','Style & Co','It''s all in the details with this lovely top from Style & Co®, featuring bell sleeves and neat pleats at its comfortably split neckline.','womens-printed-pintuck-ruffle-sleeve-top-regular-petite-created-for-macys',26.06,'images/27907595.jpg',5),
 (82,'Women''s Jacquard Striped Peasant Blouse, Created for Macy''s','Style & Co','Be the image of boho-chic in this striped peasant blouse from Style & Co®.','womens-jacquard-striped-peasant-blouse-created-for-macys',26.06,'images/27622753.jpg',5),
 (83,'Women''s 3/4-Sleeve Collared Button Down Blouse','CeCe','A sophisticated and feminine top, featuring a classic collar and split neck for an elegant and stylish finish. ABOUT THE BRAND: CeCe is a contemporary lifestyle brand inspired by a romantic take on the everyday, punctuated by taste, wit, and on-the-go flair.','womens-34-sleeve-collared-button-down-blouse',66.75,'images/30421351_fpx.jpg',5),
 (84,'Women''s Puff-Sleeve Button-Front Blouse','CeCe','Instantly elevate your style with this puff-sleeve blouse from CeCe, featuring ruffled trim. ABOUT THE BRAND: CeCe is a contemporary lifestyle brand inspired by a romantic take on the everyday, punctuated by taste, wit, and on-the-go flair.','womens-puff-sleeve-button-front-blouse',41.4,'images/29694941_fpx.jpg',5),
 (85,'Women''s 3/4-Sleeve Collared Button Down Blouse','CeCe','A sophisticated and feminine top, featuring a classic collar and split neck for an elegant and stylish finish. ABOUT THE BRAND: CeCe is a contemporary lifestyle brand inspired by a romantic take on the everyday, punctuated by taste, wit, and on-the-go flair.','womens-34-sleeve-collared-button-down-blouse',68.95,'images/28987835_fpx.jpg',5);
DROP INDEX IF EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
DROP INDEX IF EXISTS "auth_group_permissions_group_id_b120cbf9";
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
DROP INDEX IF EXISTS "auth_group_permissions_permission_id_84c5c92e";
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
DROP INDEX IF EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
DROP INDEX IF EXISTS "auth_user_groups_user_id_6a12ed8b";
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
DROP INDEX IF EXISTS "auth_user_groups_group_id_97559544";
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_user_id_a95ead1b";
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
DROP INDEX IF EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c";
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
DROP INDEX IF EXISTS "django_admin_log_content_type_id_c4bce8eb";
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
DROP INDEX IF EXISTS "django_admin_log_user_id_c564eba6";
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
DROP INDEX IF EXISTS "django_content_type_app_label_model_76bd3d3b_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
DROP INDEX IF EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
DROP INDEX IF EXISTS "auth_permission_content_type_id_2f476e4b";
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
DROP INDEX IF EXISTS "store_category_name_150032c6";
CREATE INDEX IF NOT EXISTS "store_category_name_150032c6" ON "store_category" (
	"name"
);
DROP INDEX IF EXISTS "store_product_slug_6de8ee4b";
CREATE INDEX IF NOT EXISTS "store_product_slug_6de8ee4b" ON "store_product" (
	"slug"
);
DROP INDEX IF EXISTS "store_product_category_id_574bae65";
CREATE INDEX IF NOT EXISTS "store_product_category_id_574bae65" ON "store_product" (
	"category_id"
);
DROP INDEX IF EXISTS "payment_order_user_id_5d749f62";
CREATE INDEX IF NOT EXISTS "payment_order_user_id_5d749f62" ON "payment_order" (
	"user_id"
);
DROP INDEX IF EXISTS "payment_orderitem_order_id_32d59828";
CREATE INDEX IF NOT EXISTS "payment_orderitem_order_id_32d59828" ON "payment_orderitem" (
	"order_id"
);
DROP INDEX IF EXISTS "payment_orderitem_product_id_6a98ebcd";
CREATE INDEX IF NOT EXISTS "payment_orderitem_product_id_6a98ebcd" ON "payment_orderitem" (
	"product_id"
);
DROP INDEX IF EXISTS "payment_orderitem_user_id_81163bf1";
CREATE INDEX IF NOT EXISTS "payment_orderitem_user_id_81163bf1" ON "payment_orderitem" (
	"user_id"
);
DROP INDEX IF EXISTS "payment_shippingaddress_user_id_2f4d274e";
CREATE INDEX IF NOT EXISTS "payment_shippingaddress_user_id_2f4d274e" ON "payment_shippingaddress" (
	"user_id"
);
DROP INDEX IF EXISTS "django_session_expire_date_a5c62663";
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
