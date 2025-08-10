import { CheckCircle, Eye, EyeOff, XCircle } from 'lucide-react';
import { useMemo, useState } from 'react';

import { Markdown } from '@/components/Markdown';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

interface MCQOption {
  id: string;
  text: string;
  isCorrect: boolean;
  explanation?: string;
}

interface MCQProps {
  question: string;
  options: MCQOption[];
  selected_option?: string | null;
  selected_options?: string[];
  revealed: boolean;
  allow_multiple?: boolean;
  name?: string;
}

const MCQ = ({
  question,
  options,
  selected_option: initialSelectedOption,
  selected_options: initialSelectedOptions,
  revealed: initialRevealed,
  allow_multiple = false,
  name
}: MCQProps) => {
  const [selectedOption, setSelectedOption] = useState<string | null>(
    initialSelectedOption || null
  );
  const [selectedOptions, setSelectedOptions] = useState<string[]>(
    initialSelectedOptions || []
  );
  const [revealed, setRevealed] = useState(initialRevealed);
  const [hasSubmitted, setHasSubmitted] = useState(
    !!(
      initialSelectedOption ||
      (initialSelectedOptions && initialSelectedOptions.length > 0)
    )
  );

  const handleOptionSelect = (optionId: string) => {
    if (hasSubmitted) return;

    if (allow_multiple) {
      // Handle multiple selection with checkboxes
      setSelectedOptions((prev) => {
        if (prev.includes(optionId)) {
          return prev.filter((id) => id !== optionId);
        } else {
          return [...prev, optionId];
        }
      });
    } else {
      setSelectedOption(optionId);
    }
  };

  const handleSubmit = () => {
    if (allow_multiple ? selectedOptions.length > 0 : selectedOption) {
      setHasSubmitted(true);
    }
  };

  const handleReveal = () => {
    setRevealed(!revealed);
  };

  const handleTryAgain = () => {
    setSelectedOption(null);
    setSelectedOptions([]);
    setHasSubmitted(false);
    setRevealed(false);
  };

  const selectedOptionData = options.find((opt) => opt.id === selectedOption);

  // Calculate correctness for single vs multiple selection
  const isCorrect = useMemo(() => {
    if (!hasSubmitted) return false;

    if (allow_multiple) {
      // For multiple selection, all selected options must be correct AND all correct options must be selected
      const correctOptionIds = options
        .filter((opt) => opt.isCorrect)
        .map((opt) => opt.id);
      const selectedSet = new Set(selectedOptions);
      const correctSet = new Set(correctOptionIds);

      return (
        selectedSet.size === correctSet.size &&
        [...selectedSet].every((id) => correctSet.has(id))
      );
    } else {
      // For single selection, just check if the selected option is correct
      return selectedOptionData?.isCorrect || false;
    }
  }, [
    hasSubmitted,
    allow_multiple,
    selectedOptions,
    selectedOptionData,
    options
  ]);

  const correctOption = options.find((opt) => opt.isCorrect);

  return (
    <Card className="w-full max-w-2xl mx-auto border-2 border-primary/20 bg-card">
      <CardHeader className="pb-4">
        <div className="flex items-center justify-between">
          <CardTitle className="text-lg font-semibold text-foreground flex items-center gap-2">
            🎯 {name || 'Multiple Choice Question'}
          </CardTitle>
          <Badge variant="secondary" className="bg-primary/10 text-primary">
            {allow_multiple ? 'Multiple Choice' : 'Single Choice'}
          </Badge>
        </div>
      </CardHeader>

      <CardContent className="space-y-4">
        {/* Question */}
        <div className="bg-muted/50 p-4 rounded-lg border border-border">
          <h3 className="font-medium text-foreground mb-2">Question:</h3>
          <div className="text-muted-foreground">
            <Markdown allowHtml={false} latex={true}>
              {question}
            </Markdown>
          </div>
        </div>

        {/* Options */}
        <div className="space-y-3">
          <label className="block text-sm font-medium text-foreground">
            Select your answer:
          </label>
          <div className="space-y-2">
            {options.map((option) => {
              const isSelected = allow_multiple
                ? selectedOptions.includes(option.id)
                : selectedOption === option.id;
              const showAsCorrect = revealed && option.isCorrect;
              const showAsIncorrect =
                revealed && !option.isCorrect && isSelected;

              return (
                <div
                  key={option.id}
                  onClick={() => handleOptionSelect(option.id)}
                  className={`
                    p-4 rounded-lg border cursor-pointer transition-all duration-200
                    ${hasSubmitted ? 'cursor-not-allowed' : 'hover:bg-muted/30'}
                    ${
                      isSelected && !revealed
                        ? 'border-primary bg-primary/10'
                        : 'border-border'
                    }
                    ${
                      showAsCorrect
                        ? 'border-green-500 bg-green-50 dark:bg-green-950/20'
                        : ''
                    }
                    ${
                      showAsIncorrect
                        ? 'border-red-500 bg-red-50 dark:bg-red-950/20'
                        : ''
                    }
                    ${!isSelected && !revealed ? 'hover:border-primary/50' : ''}
                  `}
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      <div
                        className={`
                        w-4 h-4 border-2 flex items-center justify-center
                        ${allow_multiple ? 'rounded' : 'rounded-full'}
                        ${
                          isSelected && !revealed
                            ? 'border-primary bg-primary'
                            : 'border-muted-foreground'
                        }
                        ${showAsCorrect ? 'border-green-500 bg-green-500' : ''}
                        ${showAsIncorrect ? 'border-red-500 bg-red-500' : ''}
                      `}
                      >
                        {(isSelected || showAsCorrect) && (
                          <div
                            className={`w-2 h-2 bg-white ${
                              allow_multiple ? 'rounded-sm' : 'rounded-full'
                            }`}
                          />
                        )}
                      </div>
                      <div
                        className={`
                        font-medium
                        ${
                          showAsCorrect
                            ? 'text-green-800 dark:text-green-300'
                            : ''
                        }
                        ${
                          showAsIncorrect
                            ? 'text-red-800 dark:text-red-300'
                            : ''
                        }
                        ${!revealed ? 'text-foreground' : ''}
                      `}
                      >
                        <Markdown allowHtml={false} latex={true}>
                          {option.text}
                        </Markdown>
                      </div>
                    </div>

                    {revealed && option.isCorrect && (
                      <CheckCircle className="w-5 h-5 text-green-600 dark:text-green-400" />
                    )}
                    {revealed && !option.isCorrect && isSelected && (
                      <XCircle className="w-5 h-5 text-red-600 dark:text-red-400" />
                    )}
                  </div>

                  {/* Show explanation if revealed and option has one */}
                  {revealed &&
                    option.explanation &&
                    (isSelected || option.isCorrect) && (
                      <div className="mt-3 pt-3 border-t border-border">
                        <div className="text-sm text-muted-foreground">
                          <strong>Explanation:</strong>{' '}
                          <Markdown allowHtml={false} latex={true}>
                            {option.explanation}
                          </Markdown>
                        </div>
                      </div>
                    )}
                </div>
              );
            })}
          </div>

          {/* Submit Button */}
          {!hasSubmitted && (
            <Button
              onClick={handleSubmit}
              disabled={
                allow_multiple ? selectedOptions.length === 0 : !selectedOption
              }
              className="w-full bg-primary hover:bg-primary/90 text-primary-foreground"
            >
              Submit Answer
            </Button>
          )}
        </div>

        {/* Feedback */}
        {hasSubmitted && (
          <div
            className={`p-4 rounded-lg border ${
              isCorrect
                ? 'bg-green-50 dark:bg-green-950/20 border-green-200 dark:border-green-800'
                : 'bg-red-50 dark:bg-red-950/20 border-red-200 dark:border-red-800'
            }`}
          >
            <div className="flex items-center gap-2 mb-2">
              {isCorrect ? (
                <>
                  <CheckCircle className="w-5 h-5 text-green-600 dark:text-green-400" />
                  <span className="font-medium text-green-800 dark:text-green-300">
                    Correct!
                  </span>
                </>
              ) : (
                <>
                  <XCircle className="w-5 h-5 text-red-600 dark:text-red-400" />
                  <span className="font-medium text-red-800 dark:text-red-300">
                    Incorrect
                  </span>
                </>
              )}
            </div>
            <div className="text-sm text-muted-foreground">
              {isCorrect ? (
                'Great job! You selected the correct answer.'
              ) : (
                <span>
                  {allow_multiple ? (
                    selectedOptions.length > 0 ? (
                      <>
                        You selected:{' '}
                        {selectedOptions.map((optionId, index) => {
                          const option = options.find(
                            (opt) => opt.id === optionId
                          );
                          return (
                            <span key={optionId}>
                              {index > 0 && ', '}"
                              <Markdown
                                allowHtml={false}
                                latex={true}
                                className="inline"
                              >
                                {option?.text || ''}
                              </Markdown>
                              "
                            </span>
                          );
                        })}
                        .{' '}
                      </>
                    ) : (
                      'No options selected. '
                    )
                  ) : (
                    <>
                      You selected "
                      <Markdown
                        allowHtml={false}
                        latex={true}
                        className="inline"
                      >
                        {selectedOptionData?.text || ''}
                      </Markdown>
                      ".{' '}
                    </>
                  )}
                  {revealed
                    ? ''
                    : 'Click "Show Answer" to see the correct response.'}
                </span>
              )}
            </div>
          </div>
        )}

        {/* Show Answer / Try Again */}
        <div className="flex gap-2">
          <Button onClick={handleReveal} variant="outline" className="flex-1">
            {revealed ? (
              <>
                <EyeOff className="w-4 h-4 mr-2" />
                Hide Answer
              </>
            ) : (
              <>
                <Eye className="w-4 h-4 mr-2" />
                Show Answer
              </>
            )}
          </Button>

          {hasSubmitted && !isCorrect && (
            <Button
              onClick={handleTryAgain}
              className="flex-1 bg-primary hover:bg-primary/90 text-primary-foreground"
            >
              Try Again
            </Button>
          )}
        </div>

        {/* Correct Answer Display */}
        {revealed && (
          <div className="bg-yellow-50 dark:bg-yellow-950/20 border border-yellow-200 dark:border-yellow-800 p-4 rounded-lg">
            <h4 className="font-medium text-yellow-800 dark:text-yellow-300 mb-2">
              {allow_multiple ? 'Correct Answers:' : 'Correct Answer:'}
            </h4>
            {allow_multiple ? (
              <div className="space-y-2">
                {options
                  .filter((opt) => opt.isCorrect)
                  .map((option) => (
                    <div
                      key={option.id}
                      className="text-yellow-700 dark:text-yellow-200 font-medium"
                    >
                      <Markdown allowHtml={false} latex={true}>
                        {option.text}
                      </Markdown>
                      {option.explanation && (
                        <div className="text-sm text-yellow-600 dark:text-yellow-300 mt-1">
                          <Markdown allowHtml={false} latex={true}>
                            {option.explanation}
                          </Markdown>
                        </div>
                      )}
                    </div>
                  ))}
              </div>
            ) : (
              <>
                <div className="text-yellow-700 dark:text-yellow-200 font-medium">
                  <Markdown allowHtml={false} latex={true}>
                    {correctOption?.text || ''}
                  </Markdown>
                </div>
                {correctOption?.explanation && (
                  <div className="text-sm text-yellow-600 dark:text-yellow-300 mt-2">
                    <Markdown allowHtml={false} latex={true}>
                      {correctOption.explanation}
                    </Markdown>
                  </div>
                )}
              </>
            )}
          </div>
        )}
      </CardContent>
    </Card>
  );
};

export default MCQ;
