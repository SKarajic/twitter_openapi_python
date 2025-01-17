# MediaExtended


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_media_info** | [**AdditionalMediaInfo**](AdditionalMediaInfo.md) |  | [optional] 
**display_url** | **str** |  | 
**expanded_url** | **str** |  | 
**ext_media_availability** | [**ExtMediaAvailability**](ExtMediaAvailability.md) |  | 
**features** | **object** |  | [optional] 
**id_str** | **str** |  | 
**indices** | **List[int]** |  | 
**media_stats** | [**MediaStats**](MediaStats.md) |  | [optional] 
**media_key** | **str** |  | 
**media_url_https** | **str** |  | 
**original_info** | [**MediaOriginalInfo**](MediaOriginalInfo.md) |  | 
**sizes** | [**MediaSizes**](MediaSizes.md) |  | 
**type** | **str** |  | 
**url** | **str** |  | 
**video_info** | [**MediaVideoInfo**](MediaVideoInfo.md) |  | [optional] 

## Example

```python
from twitter_openapi_python_generated.models.media_extended import MediaExtended

# TODO update the JSON string below
json = "{}"
# create an instance of MediaExtended from a JSON string
media_extended_instance = MediaExtended.from_json(json)
# print the JSON string representation of the object
print MediaExtended.to_json()

# convert the object into a dict
media_extended_dict = media_extended_instance.to_dict()
# create an instance of MediaExtended from a dict
media_extended_form_dict = media_extended.from_dict(media_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


