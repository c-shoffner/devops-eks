cluster_name="liatrio-eks-0XoKiTgg"
cluster_region="us-west-2"
# aws eks update-kubeconfig --name $(terraform output -raw cluster_name) --region $(terraform output -raw region)
aws eks update-kubeconfig --name $cluster_name --region $cluster_region