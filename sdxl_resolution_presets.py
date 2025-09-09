import nodes

class SDXLResolutionPresets:
    RESOLUTIONS = [
        "640x1536 | 5:12",
        "768x1344 | 4:7",
        "832x1216 | 13:19",
        "896x1152 | 7:9",
        "1024x1024 | 1:1",
        "1152x896 | 9:7",
        "1216x832 | 19:13",
        "1344x768 | 7:4",
        "1536x640 | 12:5"
    ]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": (
                    SDXLResolutionPresets.RESOLUTIONS, 
                    { "default": "1024x1024 | 1:1" }
                )
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_value"

    CATEGORY = "utils"

    def get_value(self, resolution: str) -> tuple[int, int]:
        match resolution:
            case "640x1536 | 5:12":
                return (640, 1536)
            case "768x1344 | 4:7":
                return (768, 1344)
            case "832x1216 | 13:19":
                return (832, 1216)
            case "896x1152 | 7:9":
                return (896, 1152)
            case "1024x1024 | 1:1":
                return (1024, 1024)
            case "1152x896 | 9:7":
                return (1152, 896)
            case "1216x832 | 19:13":
                return (1216, 832)
            case "1344x768 | 7:4":
                return (1344, 768)
            case "1536x640 | 12:5":
                return (1536, 640)

NODE_CLASS_MAPPINGS = {
    "SDXLResolutionPresets": SDXLResolutionPresets,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLResolutionPresets": "SDXL Resolution Presets",
}
