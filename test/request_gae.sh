get_url="https://term-project-elastic-inference.ue.r.appspot.com/"
post_url="https://term-project-elastic-inference.ue.r.appspot.com/mnist"

# curl -i -X GET $get_url

curl -i -X POST --header "Content-Type: image/jpeg" \
    --data-binary "@/home/dansun47/Elastic-Inference/test/test_data/img_1.jpg" \
    $post_url