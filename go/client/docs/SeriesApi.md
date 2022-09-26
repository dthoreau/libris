# {{classname}}

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**SeriesGet**](SeriesApi.md#SeriesGet) | **Get** /series | List of books in this series
[**SubjectsGet**](SeriesApi.md#SubjectsGet) | **Get** /subjects | list of books in subject

# **SeriesGet**
> []Isbn SeriesGet(ctx, series)
List of books in this series

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **series** | [**string**](.md)|  | 

### Return type

[**[]Isbn**](ISBN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **SubjectsGet**
> []Isbn SubjectsGet(ctx, subject)
list of books in subject

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **subject** | [**string**](.md)|  | 

### Return type

[**[]Isbn**](ISBN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

