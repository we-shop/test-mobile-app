from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR PROFILE PAGE MODEL
FOLLOWERS_COUNT = "com.socialsuperstore:id/profileFollowersCount"
FOLLOWINGS_COUNT = "com.socialsuperstore:id/profileFollowingCount"
FOLLOWERS_LABEL_PROFILE = "com.socialsuperstore:id/profileFollowersTitle"
FOLLOWINGS_LABEL_PROFILE = "com.socialsuperstore:id/profileFollowingTitle"
WISHLIST_LABEL_PROFILE = "com.socialsuperstore:id/profileWishlistsTitle"
PROFILE_FIRST_AND_LAST_NAME = "com.socialsuperstore:id/nameTextView"
PROFILE_USERNAME = "com.socialsuperstore:id/usernameTextView"
PROFILE_BIO = "com.socialsuperstore:id/userDescriptionTextView"
PROFILE_SETTINGS_BTN = "com.socialsuperstore:id/settingsBtn"
PROFILE_SETTINGS_EDIT_BTN = "com.socialsuperstore.feature_settings:id/editProfileBtn"
FOOTER_ITEM_HOME = "Home"
FOOTER_ITEM_DASHBOARD = "Rewards"
PLUS_BUTTON = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageButton"
FOOTER_ITEM_NEW_POST = "New post"
FOOTER_ITEM_INBOX = "Alerts"
FOOTER_ITEM_PROFILE = "Profile"
PROFILE_POSTS_TAB = "Posts"
PROFILE_WISHLIST_TAB = "Wishlists"
PROFILE_FIRST_ITEM_IN_POSTS_TAB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView"
PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT = "//android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[2]"
PROFILE_FIRST_ITEM_IN_POST_TAB_TEXT_SPECIAL = "//android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[1]"
PROFILE_FIRST_ITEM_IN_WISHLIST_GRID = "//*[contains(@resource-id, 'titleText')]"
PROFILE_FIRST_ITEM_TEXT_INSED_WISHLIST = "com.socialsuperstore:id/titleTextView"
NESTED_PRODUCTS_COUNT_IN_POST = "//android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView[1]"
POST_PRODUCT_TITLE = "com.socialsuperstore:id/productTitle"
PROFILE_QUESTIONS_TAB = "Questions"
FIRST_QUESTION_IN_QUEST_TAB = "//android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView[2]"
PROFILE_FOLLOWERS_TAB_FOLLOWERS_TAB = "Followers"
PROFILE_FOLLOWERS_TAB_FOLLOWINGS_TAB = "Following"
PROFILE_FOLLOWERS_TAB_ALL_ITEMS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.CompoundButton"
PROFILE_EDIT_PHOTO_CHANGE_ICON = "com.socialsuperstore.feature_settings:id/changePhotoBtn" #"com.socialsuperstore.feature_settings:id/pickImageEmptyCamera"
PROFILE_EDIT_PHOTO_CHANGE_TAKE_PHOTO = "//androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[1]"
PROFILE_EDIT_PHOTO_CHANGE_PICK_PHOTO = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat[2]"
PROFILE_EDIT_FIRST_NAME_FIELD = "//*[contains(@resource-id, 'firstNameInput')]//android.widget.EditText" #"com.socialsuperstore.feature_settings:id/firstNameInput"
PROFILE_EDIT_LAST_NAME_FIELD =  "//*[contains(@resource-id, 'lastNameInput')]//android.widget.EditText" #"com.socialsuperstore.feature_settings:id/lastNameInput"
PROFILE_EDIT_BIO_FIELD = "//*[contains(@resource-id, 'bioInput')]//android.widget.EditText" #"com.socialsuperstore.feature_settings:id/bioInput"
PROFILE_EDIT_INTERESTS_ALL_CHECKBOXES = "//*[contains(@resource-id, 'checkbox')]"
PROFILE_EDIT_SAVE_CHANGES_BTN = "com.socialsuperstore.feature_settings:id/saveBtn" #"com.socialsuperstore.feature_settings:id/saveChangesButton"
PROFILE_SETTINGS_FULL_NAME_TEXT = "com.socialsuperstore.feature_settings:id/userFullNameTextView"
PROFILE_SETTINGS_USERNAME_TEXT = "com.socialsuperstore.feature_settings:id/userNickNameTextView"
BACK_BTN = "Navigate up"

# SETTINGS MENU ITEMS
SETTINGS_MANAGE_YOUR_CREDS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[1]"
SETTINGS_NOTIFICATION_N_COMMUNICATION = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[2]"
SETTINGS_SOCIAL_CONNECT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[1]/android.view.ViewGroup[3]"

SETTINGS_LEGAL_N_TERMS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[1]"
SETTINGS_CUSTOMER_SUPPORT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[2]"
SETTINGS_ABOUT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[3]"
SETTINGS_DEBUG_INFO = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[2]/android.view.ViewGroup[4]"

SETTINGS_DEACTIVATE_ACC = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[3]/android.view.ViewGroup[1]"
SETTINGS_SIGN_OUT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView[3]/android.view.ViewGroup[2]"

# DEACTIVATE ACC
DEACTIVATE_ACCOUNT_BTN = "com.socialsuperstore.feature_settings:id/deactivateAccountButton"
DEACTIVATE_ACC_ACCEPT_IN_MODAL = "com.socialsuperstore:id/deactivateAccountButton"
ALREADY_HAVE_ACC_LOGIN_SCREEN = "com.socialsuperstore:id/signInBtn"
READ_WELCOME_TEXT_LOGIN_SCREEN = "com.socialsuperstore.feature_native_auth:id/loginTitle"

# FOLLOWERS/FOLLOWING TABS
LIST_OF_ALL_FOLLOW_BTNS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.CompoundButton"
FIRST_BTN_IN_FOLLOWERS_TAB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.CompoundButton"
SECOND_BTN_IN_FOLLOWERS_TAB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.CompoundButton"
THIRD_BTN_IN_FOLLOWERS_TAB = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.CompoundButton"

# OTHER USER PROFILE VIEW
FOLLOW_TO_USER_BTN = "com.socialsuperstore:id/followButton"

# WESHOP INFO PAGES
MENU_TERMS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]"
MENU_POLICY = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]"
MENU_COOKIE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[3]"
MENU_ACKNOWLEDGEMENTS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[4]"
MENU_COMMUNITY_GUIDES = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[5]"
TERMS_PAGE_TEXT_TITLE = "weshop-terms-of-service"
PRIVACY_POLICY_TITLE = "privacy-policy"
COOKIE_POLICY_TITLE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.widget.TextView"
ACKNOWLEDGEMENTS_TITLE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.widget.TextView"
COMMUNITY_GUIDELINES_TITLE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View/android.view.View/android.widget.TextView"
BROWSER_URL_BAR = "com.android.chrome:id/url_bar"

# SETINGS > ABOUT
APP_VERSION_SETTINGS_ABOUT = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]"
	
#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView
#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView[2]