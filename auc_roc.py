from sklearn.metrics import roc_auc_score, precision_score

def evaluate_model(input_dict):
    # Your code here
    true_labels = input_dict['true_labels']
    best_model = ('random_classifier', 0.5, 0.0)

    for model_name, predicted_labels in input_dict.items():
        if model_name == 'true_labels':
            continue
        
        roc_auc = roc_auc_score(true_labels, predicted_labels)
        precision = precision_score(true_labels, predicted_labels)
        
        if (roc_auc > best_model[1]) or (roc_auc == best_model[1] and precision > best_model[2]):
            best_model = (model_name, roc_auc, precision)
    
    return best_model[0], round(best_model[1], 2), round(best_model[2], 2)

if _name_ == "_main_":
    input_dict = eval(input())
 …
