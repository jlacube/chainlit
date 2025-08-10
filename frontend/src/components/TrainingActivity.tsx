import { CheckCircle, Eye, EyeOff, XCircle } from 'lucide-react';
import { useState } from 'react';

import { Markdown } from '@/components/Markdown';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';

interface TrainingActivityProps {
  question: string;
  hidden_answer: string;
  user_answer?: string | null;
  revealed: boolean;
  name?: string;
}

const TrainingActivity = ({
  question,
  hidden_answer,
  user_answer: initialUserAnswer,
  revealed: initialRevealed,
  name
}: TrainingActivityProps) => {
  const [userAnswer, setUserAnswer] = useState(initialUserAnswer || '');
  const [revealed, setRevealed] = useState(initialRevealed);
  const [hasSubmitted, setHasSubmitted] = useState(!!initialUserAnswer);

  const handleSubmit = () => {
    if (userAnswer.trim()) {
      setHasSubmitted(true);
    }
  };

  const handleReveal = () => {
    setRevealed(!revealed);
  };

  const isCorrect =
    hasSubmitted &&
    userAnswer.trim().toLowerCase() === hidden_answer.toLowerCase();
  const hasAnswer = userAnswer.trim().length > 0;

  return (
    <Card className="w-full max-w-2xl mx-auto border-2 border-primary/20 bg-card">
      <CardHeader className="pb-4">
        <div className="flex items-center justify-between">
          <CardTitle className="text-lg font-semibold text-foreground flex items-center gap-2">
            🎯 {name || 'Training Activity'}
          </CardTitle>
          <Badge variant="secondary" className="bg-primary/10 text-primary">
            Interactive
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

        {/* Answer Input */}
        <div className="space-y-3">
          <label className="block text-sm font-medium text-foreground">
            Your Answer:
          </label>
          <div className="flex gap-2">
            <Input
              type="text"
              value={userAnswer}
              onChange={(e) => setUserAnswer(e.target.value)}
              placeholder="Type your answer here..."
              disabled={hasSubmitted}
              className={`flex-1 ${
                hasSubmitted
                  ? isCorrect
                    ? 'border-green-500 bg-green-50 dark:bg-green-950/20'
                    : 'border-red-500 bg-red-50 dark:bg-red-950/20'
                  : ''
              }`}
              onKeyPress={(e) => {
                if (e.key === 'Enter' && !hasSubmitted && hasAnswer) {
                  handleSubmit();
                }
              }}
            />
            {!hasSubmitted && (
              <Button
                onClick={handleSubmit}
                disabled={!hasAnswer}
                className="bg-primary hover:bg-primary/90 text-primary-foreground"
              >
                Submit
              </Button>
            )}
          </div>
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
                    Not quite right
                  </span>
                </>
              )}
            </div>
            <p className="text-sm text-muted-foreground">
              {isCorrect
                ? 'Great job! You got it right.'
                : 'Try again or reveal the answer to see the correct response.'}
            </p>
          </div>
        )}

        {/* Answer Reveal */}
        <div className="space-y-3">
          <Button onClick={handleReveal} variant="outline" className="w-full">
            {revealed ? (
              <>
                <EyeOff className="w-4 h-4 mr-2" />
                Hide Answer
              </>
            ) : (
              <>
                <Eye className="w-4 h-4 mr-2" />
                Reveal Answer
              </>
            )}
          </Button>

          {revealed && (
            <div className="bg-yellow-50 dark:bg-yellow-950/20 border border-yellow-200 dark:border-yellow-800 p-4 rounded-lg">
              <h4 className="font-medium text-yellow-800 dark:text-yellow-300 mb-2">
                Correct Answer:
              </h4>
              <div className="text-yellow-700 dark:text-yellow-200 font-medium">
                <Markdown allowHtml={false} latex={true}>
                  {hidden_answer}
                </Markdown>
              </div>
            </div>
          )}
        </div>

        {/* Try Again */}
        {hasSubmitted && !isCorrect && (
          <Button
            onClick={() => {
              setUserAnswer('');
              setHasSubmitted(false);
            }}
            className="w-full bg-primary hover:bg-primary/90 text-primary-foreground"
          >
            Try Again
          </Button>
        )}
      </CardContent>
    </Card>
  );
};

export default TrainingActivity;
