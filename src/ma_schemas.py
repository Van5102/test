from .extentsion import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("customer_name", "food_name", "quantity", "price")
class TicketSchema(ma.Schema):
    class Meta:
        fields = ("food_name", "Total_Quantity")
class CustomerSchema(ma.Schema):
    class Meta:
        fields = ("customer_name", "customer_phone", "customer_address")	