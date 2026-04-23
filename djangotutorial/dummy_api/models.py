from django.db import models


class User(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    maiden_name = models.CharField()
    age = models.IntegerField()
    gender = models.CharField()
    email = models.EmailField()
    phone = models.CharField()
    username = models.CharField()
    password = models.CharField()
    birthday = models.DateField()
    image = models.URLField()
    blood_group = models.CharField()
    height = models.FloatField()
    weight = models.FloatField()
    eye_color = models.CharField()
    hair_color = models.CharField()
    hair_type = models.CharField()
    ip = models.GenericIPAddressField()
    address = models.CharField()
    city = models.CharField()
    state = models.CharField()
    state_code = models.CharField()
    postal_code = models.CharField()
    coordinates = models.CharField()
    country = models.CharField()
    mac_address = models.CharField()
    university = models.CharField()
    bank_card_expire = models.CharField()
    bank_card_number = models.CharField()
    bank_card_type = models.CharField()
    bank_currency = models.CharField()
    bank_iban = models.CharField()
    company_department = models.CharField()
    company_name = models.CharField()
    company_title = models.CharField()
    company_address = models.CharField()
    company_city = models.CharField()
    company_state = models.CharField()
    company_state_code = models.CharField()
    company_postal_code = models.CharField()
    company_coordinates = models.CharField()
    company_country = models.CharField()
    ein = models.CharField()
    ssn = models.CharField()
    user_agent = models.CharField()
    crypto_coint = models.CharField()
    crypto_wallet = models.CharField()
    crypto_network = models.CharField()
    role = models.CharField()


class Todo(models.Model):
    title = models.CharField()
    completed = models.BooleanField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Recipe(models.Model):
    name = models.CharField()
    ingredients = models.CharField()
    instructions = models.CharField()
    prep_time_minutes = models.IntegerField()
    cook_time_minutes = models.IntegerField()
    servings = models.IntegerField()
    difficulty = models.CharField()
    cuisine = models.CharField()
    calories_per_serving = models.IntegerField()
    tags = models.CharField()
    image = models.URLField()
    rating = models.FloatField()
    review_count = models.IntegerField()
    meal_type = models.CharField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Quote(models.Model):
    title = models.CharField()
    author = models.CharField()


class Product(models.Model):
    title = models.CharField()
    description = models.CharField()
    category = models.CharField()
    price = models.FloatField()
    discount_percentage = models.FloatField()
    rating = models.FloatField()
    stock = models.IntegerField()
    tags = models.CharField()
    brand = models.CharField()
    sku = models.CharField()
    weight = models.IntegerField()
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    warranty_information = models.CharField()
    shipping_information = models.CharField()
    availability_status = models.CharField()
    return_policy = models.CharField()
    minimum_order_quantity = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    barcode = models.CharField()
    qr_code = models.CharField()
    thumbnail = models.URLField()


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.CharField()
    date = models.DateTimeField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField()
    body = models.CharField()
    tags = models.CharField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    views = models.IntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    body = models.CharField()
    likes = models.IntegerField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
