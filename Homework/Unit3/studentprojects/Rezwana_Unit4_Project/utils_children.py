# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 20:39:06 2020

@author: Jonathan
"""
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score

def get_val_scores(model, X, y, return_test_score=False, return_importances=False, random_state=None, randomize=True, cv=5, test_size=0.2, val_size=0.2, use_kfold=True, return_folds=False, stratify=False):
        
    if randomize:
        if stratify:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y, shuffle=True, random_state=random_state)
        else:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle=True, random_state=random_state)
    else:
        if stratify:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y, shuffle=False)
        else:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, shuffle=False)
    if use_kfold:
        val_scores = cross_val_score(model, X=X_train, y=y_train, cv=cv)
    else:
        if randomize:
            if stratify:
                X_train_, X_val, y_train_, y_val = train_test_split(X_train, y_train, test_size=val_size, stratify=y_train, shuffle=True)
            else:
                X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size, shuffle=True)
        else:
            if stratify:
                print("Warning! You opted to both stratify your training data and to not randomize it.  These settings are incompatible with scikit-learn.  Stratifying the data, but shuffle is being set to True")
                X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size, stratify=y_train, shuffle=True)
            else:
                X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size, shuffle=False) 
        val_score = model.fit(X_train, y_train).score(X_val, y_val)
        
    if return_importances:
        if hasattr(model, 'steps'):
            try:
                feats = pd.DataFrame({
                    'Columns': X.columns,
                    'Importance': model.steps[-1][1].feature_importances_
                }).sort_values(by='Importance', ascending=False)
            except:
                model.fit(X_train, y_train)
                feats = pd.DataFrame({
                    'Columns': X.columns,
                    'Importance': model.steps[-1][1].feature_importances_
                }).sort_values(by='Importance', ascending=False)
        else:
            try:
                feats = pd.DataFrame({
                    'Columns': X.columns,
                    'Importance': model.feature_importances_
                }).sort_values(by='Importance', ascending=False)
            except:
                mod.fit(X_train, y_train)
                feats = pd.DataFrame({
                    'Columns': X.columns,
                    'Importance': model.feature_importances_
                }).sort_values(by='Importance', ascending=False)
            
    mod_scores = {}
    try:
        mod_scores['validation_score'] = val_scores.mean()
        if return_folds:
            mod_scores['fold_scores'] = val_scores
    except:
        mod_scores['validation_score'] = val_score
        
    if return_test_score:
        model.fit(X_train, y_train)
        mod_scores['test_score'] =  model.score(X_test, y_test)
            
    if return_importances:
        return mod_scores, feats
    else:
        return mod_scores