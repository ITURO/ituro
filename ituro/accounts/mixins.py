class RemoveUsernameFieldMixin(object):
    "Removes username field from base_fields"

    def __init__(self, *args, **kwargs):
        self.base_fields.pop("username")
        super(RemoveUsernameFieldMixin, self).__init__(*args, **kwargs)
