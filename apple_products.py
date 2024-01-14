from random import choice


class Apple:
    def __init__(self):
        self.ceo = ('Steve Jobs', 'Tim Cook')
        self.products = apple_products = (
            'iPhone 13 Pro Max',
            'iPhone 13 Pro',
            'iPhone 13',
            'iPhone 12 Pro Max',
            'iPhone 12 Pro',
            'iPhone 12',
            'iPhone SE (2nd generation)',
            'iPhone 11 Pro Max',
            'iPhone 11 Pro',
            'iPhone 11',
            'iPhone XS Max',
            'iPhone XS',
            'iPhone XR',
            'iPhone X',
            'iPhone 8 Plus',
            'iPhone 8',
            'iPhone 7 Plus',
            'iPhone 7',
            'iPhone SE (1st generation)',
            'iPad Pro (12.9-inch) (5th generation)',
            'iPad Pro (11-inch) (3rd generation)',
            'iPad Pro (12.9-inch) (4th generation)',
            'iPad Pro (11-inch) (2nd generation)',
            'iPad Pro (12.9-inch) (3rd generation)',
            'iPad Pro (11-inch) (1st generation)',
            'iPad Pro (12.9-inch) (2nd generation)',
            'iPad Pro (12.9-inch) (1st generation)',
            'iPad Air (4th generation)',
            'iPad Air (3rd generation)',
            'iPad Air (2nd generation)',
            'iPad Air (1st generation)',
            'iPad (9th generation)',
            'iPad (8th generation)',
            'iPad (7th generation)',
            'iPad (6th generation)',
            'iPad mini (6th generation)',
            'iPad mini (5th generation)',
            'iPad mini (4th generation)',
            'iPad mini (3rd generation)',
            'iPad mini (2nd generation)',
            'iPad mini (1st generation)',
            'MacBook Air (M2, 2022)',
            'MacBook Pro 14-inch (M1 Pro, M1 Max)',
            'MacBook Pro 16-inch (M1 Pro, M1 Max)',
            'MacBook Air (M1, 2020)',
            'MacBook Pro 13-inch (M1, 2020)',
            'MacBook Pro 16-inch (2019)',
            'MacBook Pro 13-inch (2019)',
            'MacBook Air (2019)',
            'Mac mini (M1, 2020)',
            'Mac mini (2018)',
            'iMac (M2, 2022)',
            'iMac 24-inch (M1, 2021)',
            'iMac 27-inch (2020)',
            'iMac 21.5-inch (2019)',
            'iMac Pro (2017)',
            'Mac Pro (2019)',
            'Mac Pro (2013)',
            'Apple Watch Series 7',
            'Apple Watch SE',
            'Apple Watch Series 6',
            'Apple Watch Series 5',
            'Apple Watch Series 4',
            'AirPods Pro',
            'AirPods (3rd generation)',
            'AirPods (2nd generation)',
            'AirPods Max',
            'HomePod mini',
            'HomePod',
            'Apple TV 4K',
            'Apple TV HD',
        )


class Iphone(Apple):
    def __init__(self):
        super().__init__()
        self.iphone = [dev for dev in self.products if 'iphone' in dev.lower()]
        self.pro = [dev for dev in self.iphone if 'pro' in dev.lower()]
        self.plus = [dev for dev in self.iphone if 'plus' in dev.lower()]
        self.mini = [dev for dev in self.iphone if 'mini' in dev.lower()]


class Mac(Apple):
    def __init__(self):
        super().__init__()
        self.imac = [dev for dev in self.products if 'imac' in dev.lower()]
        self.mac = [dev for dev in self.products if 'mac' in dev.lower()]
        self.macbook = [dev for dev in self.products if 'macbook' in dev.lower()]


class Ipad(Apple):
    def __init__(self):
        super().__init__()
        self.ipad = [dev for dev in self.products if 'ipad' in dev.lower()]
        self.pro = [dev for dev in self.ipad if 'pro' in dev.lower()]
        self.mini = [dev for dev in self.ipad if 'mini' in dev.lower()]
        self.air = [dev for dev in self.ipad if 'air' in dev.lower()]


class Accessories(Apple):
    def __init__(self):
        super().__init__()
        self.airpods = [dev for dev in self.products if 'airpods' in dev.lower()]
        self.watch = [dev for dev in self.products if 'watch' in dev.lower()]
        self.homepod = [dev for dev in self.products if 'homepod' in dev.lower()]
        self.tv = [dev for dev in self.products if 'tv' in dev.lower()]


# example usage
apple, mac, iphone, ipad, accessories = Apple(), Mac(), Iphone(), Ipad(), Accessories()
print(choice(mac.macbook))
print(choice(accessories.airpods))
print(choice(iphone.pro))
print(choice(ipad.mini))
print(apple.ceo)
