# In this program, we define a set of classes used to create a marketplace for introducing
# artworks, people/organizations owning them, selling them, and buying them.

# This very first class, collects and saves the characteristics of an artwork, including
# its artist, title, medium, year, and the owner.

class Art:

    def __init__(self, artist, title, medium, year, owner = None):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner
    
    def __repr__(self):
        return '{artist}. "{title}". {year}, {medium}. {owner}, {location}.'.format(
            artist = self.artist, title = self.title, year = self.year, medium = self.medium,
             owner = self.owner.name, location = self.owner.location)

# Here we create our marketplace which has listings including the available artworks.

class Marketplace:

    def __init__(self, listings = []):
        self.listings = listings
    
    # A function for adding listings to a marketplace. We'll later define the listing class.
    def add_listing(self, new_listing):
        self.listings.append(new_listing)
    
    # A function for removing listings from a marketplace, after they are sold.
    def remove_listing(self, listing):
        self.listings.remove(listing)
    
    def show_listings(self):
        if len(self.listings) > 0:
            for item in self.listings:
                print(item)
        else: print('No listings around')

# Here we create a marketplace to put all the stuff in it.

veneer = Marketplace()

# print(veneer.show_listings)

# This class includes the information about the clients and allows them to sell/buy artworks.

class Client:

    def __init__(self, name, location, is_museum):
        self.name = name
        self.location = location
        self.is_museum = is_museum

    # A client can sell and artwork if (s)he owns it. The artwork can then be added to the
    # marketplace listings.
    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            lst = Listing(artwork, price, self)
            veneer.add_listing(lst)
    # An artwork can be bought if, first, the buyer isn't its owner, and second, the artwork
    # is available in the marketplace listings. After the purchase, the new owner will replace
    # the old one, and the artwork will be removed from the listings.
    def buy_artwork(self, artwork):
        if artwork.owner != self:
            for item in veneer.listings:
                if item.art == artwork:
                    lst_1 = item
                    artwork.owner = self
                    veneer.remove_listing(lst_1)
                    break
      
# Adding Edytta as a client. Note that for persons the location is as 'Private Collection'.
edytta = Client('Edytta Halpirt', 'Private Collection', False)

# Creating an artwork which is owned by Edytta.
girl_with_mandolin = Art('Picasso, Pablo', 'Girl with a Mandolin (Fanny Tellier)', 'oil on canvas', '1910', edytta)

# print(girl_with_mandolin)

# Creating another client which is a museum in New York.
moma = Client('The MOMA', 'New York', True)

# This class includes the information of a specific listing. Note that, in Marketplace class, the
# listing items are of listing type below.

class Listing:

    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller
    def __repr__(self):
        return '{art}, {price}'.format(art = self.art.title, price = self.price)

# Having Edytta selling the artwork, which results in the artwork to be added as a listing
# to the marketplace listings with a specific price.

edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')

veneer.show_listings()

# print(veneer.listings)

# Now MOMA buys the artwork from Edytta. Therefore, the new owner of the artwork is MOMA
# and it is removed from the listings in the marketplace.

moma.buy_artwork(girl_with_mandolin)

# print(girl_with_mandolin)

veneer.show_listings()

print('\nThanks for reviewing')

# Thanks for reviewing
