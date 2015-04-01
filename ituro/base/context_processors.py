from django.conf import settings


def categories(request):
    return {
        "CREATE_CATEGORIES": settings.CREATE_CATEGORIES,
        "UPDATE_CATEGORIES": settings.UPDATE_CATEGORIES,
        "CONFIRM_CATEGORIES": settings.CONFIRM_CATEGORIES,
        "ORDER_CATEGORIES": settings.ORDER_CATEGORIES,
        "RESULT_CATEGORIES": settings.RESULT_CATEGORIES,
    }


def permissions(request):
    return {
        "USER_REGISTER": settings.USER_REGISTER,
        "USER_UPDATE": settings.USER_UPDATE,
        "PROJECT_CREATE": settings.PROJECT_CREATE,
        "PROJECT_UPDATE": settings.PROJECT_UPDATE,
        "PROJECT_CONFIRM": settings.PROJECT_CONFIRM,
        "PROJECT_RESULTS": settings.PROJECT_RESULTS,
    }
