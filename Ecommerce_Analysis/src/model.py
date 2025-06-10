# Function to run the models
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score, precision_score, ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt


def train_evaluate_model(model, X, y, scale_data=False):
    """
    Train and evaluate classification model with cross-validation and test metrics.

    Parameters:
    - model: sklearn-like estimator (already initialized)
    - X: features (DataFrame or array)
    - y: target (Series or array)
    - scale_data: bool, if True applies StandardScaler to features

    Outputs:
    - Prints CV mean scores and test scores
    - Plots confusion matrix for test seteu 
    """

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    # Scale if requested
    if scale_data:
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # Cross-validation
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    scoring = {
        'accuracy': 'accuracy',
        'precision': 'precision',
        'recall': 'recall',
        'f1': 'f1',
        'roc_auc': 'roc_auc'
    }

    cv_results = cross_validate(
        model,
        X_train, y_train,
        cv=cv,
        scoring=scoring,
        return_train_score=False
    )

    mean_cv_scores = {
        metric: cv_results[f'test_{metric}'].mean() for metric in scoring}
    print("\nCross-Validation Mean Scores:")
    print(pd.Series(mean_cv_scores).round(4))

    # Train model on full train set
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(
        model, "predict_proba") else None

    # Calculate test scores
    test_scores = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1': f1_score(y_test, y_pred)
    }
    if y_proba is not None:
        test_scores['roc_auc'] = roc_auc_score(y_test, y_proba)

    print("\nTest Set Scores:")
    print(pd.Series(test_scores).round(4))

    # Confusion matrix plot
    conf_matrix = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=conf_matrix, display_labels=model.classes_)
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix - Test Set")
    plt.show()
