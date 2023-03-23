variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}
variable "cluster_name"{
  description = "name for the EKS cluster"
  type        = string
  default     = "liatrio"
}
