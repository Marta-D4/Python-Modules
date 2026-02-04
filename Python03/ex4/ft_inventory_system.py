#!/usr/bin/env python3

def create_inventory(player_name):
    return {
        'name': player_name,
        'items': {}
    }

def add_item(inventory, item_name, category, rarity, quantity, value):
    inventory['items'][item_name] = {
        'category': category,
        'rarity': rarity,
        'quantity': quantity,
        'value': value
    }

def inventory_value(inventory):
    total_value = 0

    for item in inventory['items'].values():
        total_value += item['quantity'] * item['value']

    return total_value

def transfer_item(from_inv, to_inv, item_name, quantity):
    if from_inv['items'].get(item_name) and from_inv['items'][item_name]['quantity'] >= quantity:
        from_inv['items'][item_name]['quantity'] -= quantity

        if item_name in to_inv['items']:
            to_inv['items'][item_name]['quantity'] += quantity
            """to_inv['items'][item_name].update({
                'quantity': to_inv['items'][item_name]['quantity'] + quantity
            })"""
        else:
            to_inv['items'][item_name] = {
                'category': from_inv['items'][item_name]['category'],
                'rarity': from_inv['items'][item_name]['rarity'],
                'quantity': quantity,
                'value': from_inv['items'][item_name]['value']
            }
        
        print(f"\n=== Transaction: {from_inv['name']} gives {to_inv['name']} {quantity} {item_name}s ===")
        print("Transaction successful!")
    else:
        print("Error: couldn´t make transfer")
        return

def print_inventory(player, inventory):
    print(f"\n=== {player}´s Inventory ===")

    num_items = 0
    total_value = 0
    # categories = {}

    for item, details in inventory['items'].items():
        item_value = details['quantity'] * details['value']
        print(
            f"{item} ({details['category']}, {details['rarity']}): "
            f"{details['quantity']}x @ {details['value']} gold each = {item_value} gold"
        )

        total_value += item_value
        num_items += details['quantity']
    
    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {num_items} items")


print("=== Player Inventory System ===")

# Creating player inventories
alice_inventory = create_inventory('Alice')
bob_inventory = create_inventory('Bob')
add_item(alice_inventory, 'sword', 'weapon', 'rare', 1, 500)
add_item(alice_inventory, 'potion', 'consumable', 'common', 5, 50)
add_item(alice_inventory, 'shield', 'armor', 'uncommon', 1, 200)

# Display inventories before transaction
print_inventory('Alice', alice_inventory)

# Make transaction
transfer_item(alice_inventory, bob_inventory, 'potion', 2)

# Display inventories after
print(f"\n=== Updated Inventories ===")
print(f"Alice potions: {alice_inventory['items']['potion']['quantity']}")
print(f"Bob potions: {bob_inventory['items']['potion']['quantity']}")

"""
#!/usr/bin/env python3

# Diccionario global para los inventarios
inventory = {
    'Alice': {
        'sword': {
            'class': 'weapon',
            'rarity': 'rare',
            'quantity': 1,
            'value': 500
        },
        'potion': {
            'class': 'consumable',
            'rarity': 'common',
            'quantity': 5,
            'value': 50
        },
        'shield': {
            'class': 'armor',
            'rarity': 'uncommon',
            'quantity': 1,
            'value': 200
        }
    },
    'Bob': {}
}

def inventory_value(player):
    total_value = 0
    for item, details in inventory[player].items():
        total_value += details['quantity'] * details['value']
    return total_value

def transfer_item(from_player, to_player, item_name, quantity):
    from_inv = inventory[from_player]
    to_inv = inventory[to_player]

    if item_name in from_inv and from_inv[item_name]['quantity'] >= quantity:
        from_inv[item_name]['quantity'] -= quantity

        if item_name in to_inv:
            to_inv[item_name]['quantity'] += quantity
        else:
            to_inv[item_name] = {
                'class': from_inv[item_name]['class'],
                'rarity': from_inv[item_name]['rarity'],
                'quantity': quantity,
                'value': from_inv[item_name]['value']
            }

        print(f"\n=== Transaction: {from_player} gives {to_player} {quantity} {item_name}s ===")
        print("Transaction successful!")
    else:
        print(f"Error: couldn't make transfer - Not enough items or item does not exist.")

def print_inventory(player):
    print(f"\n=== {player}'s Inventory ===")

    num_items = 0
    total_value = 0

    for item, details in inventory[player].items():
        item_value = details['quantity'] * details['value']
        print(
            f"{item} ({details['class']}, {details['rarity']}): "
            f"{details['quantity']}x @ {details['value']} gold each = {item_value} gold"
        )

        total_value += item_value
        num_items += details['quantity']

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {num_items} items")


print("=== Player Inventory System ===")

# Mostrar inventarios antes de la transacción
print_inventory('Alice')

transfer_item('Alice', 'Bob', 'potion', 2)

print(f"\n=== Updated Inventories ===")
print(f"Alice potions: {inventory['Alice']['potion']['quantity']}")
print(f"Bob potions: {inventory['Bob']['potion']['quantity']}")

"""