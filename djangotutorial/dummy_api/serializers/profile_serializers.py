from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    maiden_name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    birthday = serializers.DateField()
    image = serializers.URLField()
    blood_group = serializers.CharField()
    height = serializers.FloatField()
    weight = serializers.FloatField()
    eye_color = serializers.CharField()
    hair_color = serializers.CharField()
    hair_type = serializers.CharField()
    ip = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    state_code = serializers.CharField()
    postal_code = serializers.CharField()
    coordinates = serializers.CharField()
    country = serializers.CharField()
    mac_address = serializers.CharField()
    university = serializers.CharField()
    bank_card_expire = serializers.CharField()
    bank_card_number = serializers.CharField()
    bank_card_type = serializers.CharField()
    bank_currency = serializers.CharField()
    bank_iban = serializers.CharField()
    company_department = serializers.CharField()
    company_name = serializers.CharField()
    company_title = serializers.CharField()
    company_address = serializers.CharField()
    company_city = serializers.CharField()
    company_state = serializers.CharField()
    company_state_code = serializers.CharField()
    company_postal_code = serializers.CharField()
    company_coordinates = serializers.CharField()
    company_country = serializers.CharField()
    ein = serializers.CharField()
    snn = serializers.CharField()
    user_agent = serializers.CharField()
    crypto_coint = serializers.CharField()
    crypto_wallet = serializers.CharField()
    crypto_network = serializers.CharField()
    role = serializers.CharField()


class TodoProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    completed = serializers.BooleanField()


class RecipeProfileSerializer(serializers.Serializer):
    name = serializers.CharField()
    ingredients = serializers.CharField()
    instructions = serializers.CharField()
    prep_time_minutes = serializers.IntegerField()
    cook_time_minutes = serializers.IntegerField()
    servings = serializers.IntegerField()
    difficulty = serializers.CharField()
    cuisine = serializers.CharField()
    calories_per_serving = serializers.IntegerField()
    tags = serializers.CharField()
    image = serializers.URLField()
    rating = serializers.FloatField()
    review_count = serializers.IntegerField()
    meal_type = serializers.CharField()


class ReviewProfileSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    comment = serializers.CharField()
    date = serializers.DateTimeField()


class ProductProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    discount_percentage = serializers.FloatField()
    rating = serializers.FloatField()
    stock = serializers.IntegerField()
    tags = serializers.CharField()
    brand = serializers.CharField()
    sku = serializers.CharField()
    weight = serializers.IntegerField()
    width = serializers.FloatField()
    height = serializers.FloatField()
    depth = serializers.FloatField()
    warranty_information = serializers.CharField()
    shipping_information = serializers.CharField()
    availability_status = serializers.CharField()
    return_policy = serializers.CharField()
    minimum_order_quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    barcode = serializers.CharField()
    qr_code = serializers.CharField()
    thumbnail = serializers.URLField()


class CartProfileSerializer(serializers.Serializer):
    products = ProductProfileSerializer(many=True)


class CommentProfileSerializer(serializers.Serializer):
    body = serializers.CharField()
    likes = serializers.IntegerField()


class PostProfileSerializer(serializers.Serializer):
    title = serializers.CharField()
    body = serializers.CharField()
    tags = serializers.CharField()
    likes = serializers.IntegerField()
    dislikes = serializers.IntegerField()
    views = serializers.IntegerField()
    comments = CommentProfileSerializer(many=True)


class ProfileOutputSerializer(serializers.Serializer):
    user_info = UserProfileSerializer()
    todos = TodoProfileSerializer(many=True)
    recipes = RecipeProfileSerializer(many=True)
    reviews = ReviewProfileSerializer(many=True)
    carts = CartProfileSerializer(many=True)
    posts = PostProfileSerializer(many=True)
