from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR SEARCH PAGE MODEL
FOLLOWERS_COUNT = "com.socialsuperstore:id/profileFollowersCount"
FOLLOWINGS_COUNT = "com.socialsuperstore:id/profileFollowingCount"
FOLLOWERS_LABEL_PROFILE = "com.socialsuperstore:id/profileFollowersTitle"
FOLLOWINGS_LABEL_PROFILE = "com.socialsuperstore:id/profileFollowingTitle"
WISHLIST_LABEL_PROFILE = "com.socialsuperstore:id/profileWishlistsTitle"
PROFILE_FIRST_AND_LAST_NAME = "com.socialsuperstore:id/nameTextView"
PROFILE_USERNAME = "com.socialsuperstore:id/usernameTextView"
PROFILE_BIO = "com.socialsuperstore:id/userDescriptionTextView"
PROFILE_SETTINGS_BTN = "com.socialsuperstore:id/followButton"
PROFILE_SETTINGS_EDIT_BTN = "com.socialsuperstore.feature_settings:id/editProfileBtn"
FOOTER_ITEM_HOME = "Home"
FOOTER_ITEM_REWARDS = "Rewards"
FOOTER_ITEM_NEW_POST = "New post"
FOOTER_ITEM_ALERTS = "Alerts"
FOOTER_ITEM_PROFILE = "Profile"
PROFILE_POSTS_TAB = "Posts"
PROFILE_QUESTIONS_TAB = "Questions"
PROFILE_FOLLOWERS_TAB_FOLLOWERS_TAB = "Followers"
PROFILE_FOLLOWERS_TAB_FOLLOWINGS_TAB = "Followings"
PROFILE_FOLLOWERS_TAB_ALL_ITEMS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[1]"
PROFILE_EDIT_PHOTO_CHANGE_ICON = "com.socialsuperstore.feature_settings:id/pickImageEmptyCamera"
PROFILE_EDIT_PHOTO_CHANGE_TAKE_PHOTO = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"
PROFILE_EDIT_PHOTO_CHANGE_PICK_PHOTO = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]"
PROFILE_EDIT_FIRST_NAME_FIELD = "com.socialsuperstore.feature_settings:id/firstNameEditText"
PROFILE_EDIT_LAST_NAME_FIELD = "com.socialsuperstore.feature_settings:id/lastNameEditText"
PROFILE_EDIT_BIO_FIELD = "com.socialsuperstore.feature_settings:id/bioEditText"
PROFILE_EDIT_SAVE_CHANGES_BTN = "com.socialsuperstore.feature_settings:id/saveChangesButton"
PROFILE_SETTINGS_FULL_NAME_TEXT = "com.socialsuperstore.feature_settings:id/userFullNameTextView"
PROFILE_SETTINGS_USERNAME_TEXT = "com.socialsuperstore.feature_settings:id/userNickNameTextView"
BACK_BTN = "Перейти вверх"

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