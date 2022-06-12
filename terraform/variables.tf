variable "yandex_token" {
  description = "OAuthorization token"
  type        = string
  sensitive   = true
}

variable "yandex_cloud_id" {
  description = "Yandex compute cloud id"
  type        = string
  sensitive   = true
}

variable "yandex_folder_id" {
  description = "Yandex folder id"
  type        = string
  sensitive   = true
}

variable "yandex_cloud_image_id" {
  description = "Yandex compute cloud Linux distributive ID"
  type        = string
  default     = "fd8fte6bebi857ortlja"
  sensitive   = false
}