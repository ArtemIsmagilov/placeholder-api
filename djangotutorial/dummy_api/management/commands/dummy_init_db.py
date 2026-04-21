import json

from django.core.management.base import BaseCommand

from dummy_api.models import (
    User,
    Todo,
    Recipe,
    Quote,
    Product,
    Review,
    Post,
    Comment,
    Cart,
)


class Command(BaseCommand):
    help = "Init db from dummy json files"

    def handle(self, *args, **options):
        users_data = json.load(open("dummy-users.json"))
        users = (
            User(
                id=u["id"],
                first_name=u["firstName"],
                last_name=u["lastName"],
                maiden_name=u["maidenName"],
                age=u["age"],
                gender=u["gender"],
                email=u["email"],
                phone=u["phone"],
                username=u["username"],
                password=u["password"],
                birthday=u["birthDate"],
                image=u["image"],
                blood_group=u["bloodGroup"],
                height=u["height"],
                weight=u["weight"],
                eye_color=u["eyeColor"],
                hair_color=u["hair"]["color"],
                hair_type=u["hair"]["type"],
                ip=u["ip"],
                address=u["address"]["address"],
                city=u["address"]["city"],
                state=u["address"]["state"],
                state_code=u["address"]["stateCode"],
                postal_code=u["address"]["postalCode"],
                coordinates=f"{u['address']['coordinates']['lat']} {u['address']['coordinates']['lng']}",
                country=u["address"]["country"],
                mac_address=u["macAddress"],
                university=u["university"],
                bank_card_expire=u["bank"]["cardExpire"],
                bank_card_number=u["bank"]["cardNumber"],
                bank_card_type=u["bank"]["cardType"],
                bank_currency=u["bank"]["currency"],
                bank_iban=u["bank"]["iban"],
                company_department=u["company"]["department"],
                company_name=u["company"]["name"],
                company_title=u["company"]["title"],
                company_address=u["company"]["address"]["address"],
                company_city=u["company"]["address"]["city"],
                company_state=u["company"]["address"]["state"],
                company_state_code=u["company"]["address"]["stateCode"],
                company_postal_code=u["company"]["address"]["postalCode"],
                company_coordinates=f"{u['company']['address']['coordinates']['lat']} {u['company']['address']['coordinates']['lng']}",
                company_country=u["company"]["address"]["country"],
                ein=u["ein"],
                snn=u["ssn"],
                user_agent=u["userAgent"],
                crypto_coint=u["crypto"]["coin"],
                crypto_wallet=u["crypto"]["wallet"],
                crypto_network=u["crypto"]["network"],
                role=u["role"],
            )
            for u in users_data
        )
        User.objects.bulk_create(users)

        todos_data = json.load(open("dummy-todos.json"))
        todos = (
            Todo(
                id=t["id"],
                title=t["todo"],
                completed=t["completed"],
                user_id=t["userId"],
            )
            for t in todos_data
        )
        Todo.objects.bulk_create(todos)

        recipes_data = json.load(open("dummy-recipes.json"))
        recipes = (
            Recipe(
                id=r["id"],
                name=r["name"],
                ingredients=" | ".join(r["ingredients"]),
                instructions=" | ".join(r["instructions"]),
                prep_time_minutes=r["prepTimeMinutes"],
                cook_time_minutes=r["cookTimeMinutes"],
                servings=r["servings"],
                difficulty=r["difficulty"],
                cuisine=r["cuisine"],
                calories_per_serving=r["caloriesPerServing"],
                tags=" | ".join(r["tags"]),
                image=r["image"],
                rating=r["rating"],
                review_count=r["reviewCount"],
                meal_type=" | ".join(r["mealType"]),
                user_id=r["userId"],
            )
            for r in recipes_data
        )
        Recipe.objects.bulk_create(recipes)

        quotes_data = json.load(open("dummy-quotes.json"))
        quotes = (
            Quote(
                id=q["id"],
                title=q["quote"],
                author=q["author"],
            )
            for q in quotes_data
        )
        Quote.objects.bulk_create(quotes)

        posts_data = json.load(open("dummy-posts.json"))
        posts = (
            Post(
                id=p["id"],
                title=p["title"],
                body=p["body"],
                tags=" | ".join(p["tags"]),
                likes=p["reactions"]["likes"],
                dislikes=p["reactions"]["dislikes"],
                views=p["views"],
                user_id=p["userId"],
            )
            for p in posts_data
        )
        Post.objects.bulk_create(posts)

        products_data = json.load(open("dummy-products.json"))
        products = []
        reviews = []
        review_id = 0
        for p in products_data:
            product = Product(
                id=p["id"],
                title=p["title"],
                description=p["description"],
                category=p["category"],
                price=p["price"],
                discount_percentage=p["discountPercentage"],
                rating=p["rating"],
                stock=p["stock"],
                tags=" | ".join(p["tags"]),
                brand=p.get("brand", ""),
                sku=p["sku"],
                weight=p["weight"],
                width=p["dimensions"]["width"],
                height=p["dimensions"]["height"],
                depth=p["dimensions"]["depth"],
                warranty_information=p["warrantyInformation"],
                shipping_information=p["shippingInformation"],
                availability_status=p["availabilityStatus"],
                return_policy=p["returnPolicy"],
                minimum_order_quantity=p["minimumOrderQuantity"],
                created_at=p["meta"]["createdAt"],
                updated_at=p["meta"]["updatedAt"],
                barcode=p["meta"]["barcode"],
                qr_code=p["meta"]["qrCode"],
                thumbnail=p["thumbnail"],
            )
            products.append(product)
            for r in p["reviews"]:
                review_id += 1
                reviews.append(
                    Review(
                        id=review_id,
                        rating=r["rating"],
                        comment=r["comment"],
                        date=r["date"],
                        product_id=p["id"],
                        user_id=User.objects.get(email=r["reviewerEmail"]).id,
                    )
                )
        Product.objects.bulk_create(products)
        Review.objects.bulk_create(reviews)

        comments_data = json.load(open("dummy-comments.json"))
        comments = (
            Comment(
                id=c["id"],
                body=c["body"],
                likes=c["likes"],
                post_id=c["postId"],
            )
            for c in comments_data
        )
        Comment.objects.bulk_create(comments)

        carts_data = json.load(open("dummy-carts.json"))
        carts = (Cart(id=c["id"], user_id=c["userId"]) for c in carts_data)
        Cart.objects.bulk_create(carts)

        for cart in carts_data:
            c = Cart.objects.get(id=cart["id"])
            for prod in cart["products"]:
                c.products.add(prod["id"])

        self.stdout.write(
            self.style.SUCCESS("Successfully init db from dummy json files.")
        )
