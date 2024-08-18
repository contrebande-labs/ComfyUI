class GetImageSize:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT",)
    RETURN_NAMES = ("width", "height")
    FUNCTION = "execute"
    CATEGORY = "essentials/image utils"

    def execute(self, image):
        return (image.shape[2], image.shape[1])

