from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

# LIST OF LOCATORS FOR POST PAGE MODEL
FOOTER_ITEM_REC_PRODUCT = "//androidx.recyclerview.widget.RecyclerView/android.widget.Button[1]"
FOOTER_ITEM_ASK_QUESTION = "//androidx.recyclerview.widget.RecyclerView/android.widget.Button[2]"
SEARCH_PRODUCT_POST_CREATION = "com.socialsuperstore.feature_post_editor:id/search"
ADD_FIRST_PRODUCT_PLUS_INPUT = "//*[contains(@resource-id, 'mediaContent')]" #"/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.ImageView[1]"
SEARCH_RESULT_PRODUCT_ONE = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.CheckBox" # workable ID "//*[contains(@resource-id, 'productCheckbox')]"
SEARCH_RESULT_PRODUCT_TWO = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.CheckBox"
SEARCH_RESULT_PRODUCT_THREE = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.CheckBox"
STEP_BTN_ADD_PRODUCT = "com.socialsuperstore.feature_post_editor:id/stepBtn"
PRODUCT_ADD_FOOTER_ITEM_PRODUCTS = "Products"
PRODUCT_ADD_FOOTER_ITEM_MEDIA = "Media"
PRODUCT_ADD_FOOTER_ITEM_CAPTION = "Caption"
MEDIA_IMAGE_FROM_GALLERY = "com.socialsuperstore.feature_post_editor:id/fromGallery"
MEDIA_IMAGE_FROM_PRODUCT = "com.socialsuperstore.feature_post_editor:id/fromProductImage"
MEDIA_IMAGE_FROM_CAMERA = "com.socialsuperstore.feature_post_editor:id/fromCamera"
CAPTION_INPUT_FIELD = "com.socialsuperstore.feature_post_editor:id/captionTextInputEditText"
PUBLISH_BTN_ADD_PRODUCT = "com.socialsuperstore.feature_post_editor:id/doneBtn"
FEED_POST_DESCRIPTION = "com.socialsuperstore:id/postDescription"
POST_DOTS_SUB_MENU = "com.socialsuperstore:id/postActionsBtn"
POST_DOTS_SUB_MENU_EDIT_POST = "//androidx.recyclerview.widget.RecyclerView/android.widget.Button[1]"
POST_DOTS_SUB_MENU_DELETE_POST = "//androidx.recyclerview.widget.RecyclerView/android.widget.Button[2]"
POST_DOTS_SUB_MENU_FLAG_CONTENT_ITEMS = "com.socialsuperstore:id/actionText"
POST_FLAG_CONTENT_SUCCESS_WIN_TITLE = "com.socialsuperstore:id/title"
POST_FLAG_CONTENT_SUCCESS_WIN_DONE_BTN = "com.socialsuperstore:id/doneButton"
POST_SUB_MENU_ACTION_ITEMS_ID = "com.socialsuperstore:id/actionText"
POST_MEDIA_LAYOUT = "com.socialsuperstore:id/postProductsMediaLayout"
READ_ALL_PRODUCT_LINEAR_LAYOUTS = "//*[contains(@resource-id, 'postProductsPagerTabs')]//android.widget.LinearLayout/android.widget.LinearLayout"
READ_SINGLE_PRODUCT_LINEAR_LAYOUTS = "//*[contains(@resource-id, 'postProductsPagerTabs')]//android.widget.LinearLayout/android.widget.LinearLayout"  #'(//*[contains(@resource-id, "postProductsPagerTabs")]//android.widget.LinearLayout/android.widget.LinearLayout)[1]'
PRODUCT_EDIT_FIRST_CHECKBOX = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.CheckBox"
POST_USERNAME = "com.socialsuperstore:id/postUserName"
POST_TIME_AGO_TEXT = "com.socialsuperstore:id/timeAgoTextView"
QUESTION_TEXT_STEP_ONE = "com.socialsuperstore.feature_post_editor:id/questionTextInputEditText"
QUESTION_TEXT_MEDIA_TAB = "com.socialsuperstore.feature_post_editor:id/questionText"
QUESTION_BREAD_CRUMBS = "com.socialsuperstore:id/currentStep"
QUESTION_UPLOAD_FROM_LIBRARY = "com.socialsuperstore.feature_post_editor:id/fromGallery"
QUESTION_UPLOAD_FROM_CAMERA = "com.socialsuperstore.feature_post_editor:id/fromCamera"
QUESTION_UPLOAD_FROM_DESIGNS = "com.socialsuperstore.feature_post_editor:id/fromPopularDesigns"
QUESTION_REPLY_LABEL = "com.socialsuperstore:id/postQuestionReplyPanel"
CUSTOM_BACKGROUND_ITEMS = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView"
SAVE_BTN_BACKGROUND_ITEMS = "com.socialsuperstore:id/menuActionDone" #"com.socialsuperstore:id/submitLabel"

BACKGROUND_STYLE_AND_SIZE_TAB = "Style & size"
BACKGROUND_TEXT_COLOUR_TAB = "Text colour"
ALL_TEXT_STYLES = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout" #"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout"
TEXT_SIZE_BAR = "com.socialsuperstore.feature_post_editor:id/textSizeSeekBar"
BACKGROUND_CROP_BTN = "com.socialsuperstore.feature_post_editor:id/cropBtn"
BACKGROUND_DELETE_BTN = "com.socialsuperstore.feature_post_editor:id/deleteBtn"
ALL_TEXT_COLOURS = "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout" #"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout"
LIKES_IN_POST = "com.socialsuperstore:id/interactionsLikes"
COMMENTS_IN_POST = "com.socialsuperstore:id/interactionsComments"
GO_TO_COMMENTS_BTN = "com.socialsuperstore:id/interactionsCommentBtn"
COMMENTS_INPUT_TEXT_FIELD = "com.socialsuperstore.feature_comments:id/commentEditText"
COMMENTS_SEND_BTN = "com.socialsuperstore.feature_comments:id/sendCommentButton"
COMMENT_TEXT_ID = "com.socialsuperstore.feature_comments:id/commentTextView"
NO_COMMENTS_STUB = "com.socialsuperstore.feature_comments:id/noContentText"

# Try to adding a product first (modal in question comments)
MODAL_TITLE_TEXT = "com.socialsuperstore:id/titleTopText"
CLOSE_MODAL_BTN = "com.socialsuperstore:id/closeButton"
LET_ME_ADD_PRODUCT_FIRST_BTN = "com.socialsuperstore:id/negativeButton"
CONTINUE_WITHOUT_PRODUCT_BTN = "com.socialsuperstore:id/positiveButton"

# new post
ASK_QUESTION_PLUS_MENU = "com.socialsuperstore:id/fabAAQ"
REC_PRODUCT_PLUS_MENU = "com.socialsuperstore:id/fabRecommendProduct"

# home feed carousel
FEED_SLIDE_UPPERLINE = "//*[contains(@resource-id, 'slideSuperscript')]"
FEED_SLIDE_HEADLINE = "//*[contains(@resource-id, 'slideHeadline')]"

